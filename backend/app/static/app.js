'use strict';
const $ = id => document.getElementById(id);
const controls = ['validate-button', 'messy-button', 'corrected-button'];
let result = null;
let busy = false;

function setBusy(value) {
  busy = value;
  controls.forEach(id => { $(id).disabled = value; });
  $('register-file').disabled = value;
  $('export-button').disabled = value || !result || !result.findings.length;
  $('upload-form').setAttribute('aria-busy', String(value));
}
function resetResult() {
  result = null;
  $('results').hidden = true;
  $('getting-started').hidden = false;
  $('export-button').disabled = true;
  $('severity-filter').value = 'all';
  $('error').hidden = true;
  $('error').textContent = '';
}
function showError(message) {
  $('status').textContent = '';
  $('error').textContent = message;
  $('error').hidden = false;
}
async function responseData(response) {
  let data;
  try { data = await response.json(); }
  catch { throw new Error('The server returned an unreadable response. Please try again.'); }
  if (!response.ok) {
    throw new Error(typeof data.detail === 'string' ? data.detail : `Request failed (${response.status}). Please try again.`);
  }
  return data;
}
async function checkFile(file) {
  if (!/\.(csv|xlsx)$/i.test(file.name)) throw new Error('Choose a CSV or XLSX file.');
  if (!file.size) throw new Error('The file is empty. Choose a register with data.');
  if (file.size > 5 * 1024 * 1024) throw new Error('File exceeds the 5 MB size limit.');
  $('status').textContent = `Checking ${file.name}…`;
  const body = new FormData();
  body.append('file', file);
  const response = await fetch('/upload/risk-register', { method: 'POST', body });
  result = await responseData(response);
  renderResults();
  $('status').textContent = `Checked ${result.rows} risks. ${result.findings.length} findings returned.`;
}
async function run(action) {
  if (busy) return;
  resetResult();
  setBusy(true);
  try { await action(); }
  catch (error) { showError(error.message || 'Unable to reach AuditPilot. Check that the server is running.'); }
  finally { setBusy(false); }
}
$('upload-form').addEventListener('submit', event => {
  event.preventDefault();
  const file = $('register-file').files[0];
  if (file) run(() => checkFile(file));
});
for (const name of ['messy', 'corrected']) {
  $(`${name}-button`).addEventListener('click', () => run(async () => {
    $('register-file').value = '';
    $('status').textContent = 'Loading synthetic sample…';
    const response = await fetch(`/demo/samples/${name}.csv`, { cache: 'no-store' });
    if (!response.ok) throw new Error('The sample could not be loaded. Please try again.');
    await checkFile(new File([await response.blob()], `${name}.csv`, { type: 'text/csv' }));
  }));
}
function cell(text) {
  const td = document.createElement('td');
  td.textContent = text;
  return td;
}
function renderResults() {
  $('results').hidden = false;
  $('getting-started').hidden = true;
  $('result-title').textContent = result.findings.length ? 'A clearer list of next steps.' : 'No findings in this register.';
  $('result-file').textContent = result.filename;
  $('score').textContent = `${result.score} / 100`;
  $('score').classList.toggle('good', result.score >= 90);
  $('finding-count').textContent = result.findings.length;
  $('finding-note').textContent = result.findings.length ? 'Review each recommendation below' : 'Across the 14 implemented rules';
  $('high-count').textContent = result.findings.filter(f => ['Critical', 'High'].includes(f.severity)).length;
  $('row-count').textContent = result.rows;
  $('column-count').textContent = `${result.columns} columns checked`;
  renderFindings();
}
function renderFindings() {
  const body = $('findings-body');
  body.replaceChildren();
  const filter = $('severity-filter').value;
  const findings = result.findings.filter(f => filter === 'all' || f.severity === filter);
  for (const finding of findings) {
    const row = document.createElement('tr');
    const severity = cell('');
    const badge = document.createElement('span');
    badge.className = 'severity';
    if (['Critical', 'High', 'Medium', 'Low', 'Info'].includes(finding.severity)) badge.classList.add(finding.severity.toLowerCase());
    badge.textContent = finding.severity;
    severity.append(badge);
    const detail = cell(finding.message);
    const recommendation = document.createElement('p');
    recommendation.textContent = finding.recommendation;
    detail.append(recommendation);
    row.append(severity, cell(finding.row === 0 ? 'Whole file' : finding.row), cell(finding.column), detail);
    body.append(row);
  }
  $('empty-findings').hidden = findings.length > 0;
  $('empty-findings').textContent = result.findings.length
    ? 'No findings match this severity filter.'
    : 'No issues detected by the implemented rules. Keep reviewing risk accuracy and treatment effectiveness with your team.';
  $('export-button').disabled = busy || !result.findings.length;
}
$('severity-filter').addEventListener('change', () => { if (result) renderFindings(); });
function csvCell(value) {
  let text = String(value ?? '');
  // Prevent a spreadsheet from interpreting uploaded content as a formula.
  if (/^[\s]*[=+\-@]/.test(text)) text = `'${text}`;
  return `"${text.replaceAll('"', '""')}"`;
}
$('export-button').addEventListener('click', () => {
  if (!result || busy || !result.findings.length) return;
  const keys = ['severity', 'row', 'column', 'message', 'recommendation'];
  const csv = [keys.map(csvCell).join(','), ...result.findings.map(f => keys.map(k => csvCell(f[k])).join(','))].join('\r\n');
  const url = URL.createObjectURL(new Blob(['\ufeff', csv], { type: 'text/csv;charset=utf-8' }));
  const a = document.createElement('a');
  a.href = url;
  a.download = 'auditpilot-findings.csv';
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});
setBusy(false);
