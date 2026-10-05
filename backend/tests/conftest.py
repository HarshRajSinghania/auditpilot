from datetime import date, timedelta

import pandas as pd
import pytest


@pytest.fixture
def valid_risk_dataframe():
    review_date = (date.today() + timedelta(days=365)).isoformat()
    return pd.DataFrame(
        {
            "Risk ID": ["R001"],
            "Title": ["Weak Passwords"],
            "Description": ["Password reuse across systems"],
            "Owner": ["IT"],
            "Treatment": ["Implement MFA"],
            "Likelihood": [4],
            "Impact": [5],
            "Review Date": [review_date],
        }
    )
