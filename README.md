# JSON Data Cleaning Project (Python)
# Important Note:
This repository uses completely dummy abd fictional user data.
All emails and passwords are fake and used only for learning and data-cleaning practice.

## Problem
This project focuses on cleaning a messy JSON dataset containing user information.
The raw data had inconsistent formats, extra spaces, invalid values, and noisy fields
which made it unsuitable for analysis.

## Dataset
- Format: JSON
- Contains user details such as name, username, email, password, birth date, and preferences.

## Cleaning Steps Performed
- Converted user IDs from string to integer
- Normalized first name and last name (trimmed spaces, capitalized)
- Standardized usernames to lowercase
- Validated passwords based on length and whitespace
- Cleaned and validated email addresses
- Handled inconsistent birth date formats
- Standardized yes/no fields (married, haskids)
- Removed duplicate and empty entries from favorite movies
- Validated categorical fields like hair color and country

## Tools Used
- Python (standard library only)
- json module

## Output
The cleaned data is saved as `corrected_data.json` and is ready for analysis or further processing.
