# integrations-challenge

This tech challenge is designed to test some basic web development practices.

## To run

- Ensure you have Python 3 installed.
- Run `pip install -r requirements.txt` from the root of the repository to ensure all dependencies are installed.
- From the root of the repository, you can run any of the following three commands to perform the following actions:
  - Access: `python3 runIntegration.py ACCESS`
  - Erasure: `python3 runIntegration.py ERASURE`
  - Seed: `python3 runIntegration.py SEED`

## Mailgun Credentials

- You will be provided an API key to run this tech challenge with.

## Candidate Instructions

- Completing this practical challenge is very similar to what work would be like as an Integrations Engineer with Transcend.
  In this challenge you will be implementing a mock integration with Mailgun, an integration Transcend already offers.
- IMPORTANT: For the purposes of this challenge, we expect you to implement _ONLY_ an Access request, with the Erasure and Seeding logic as _optional_, bonus challenges.

### To implement:

You'll have to research the Mailgun API and understand how to use it! Pro-tip: `/v3/domains` is where you can fetch the list of domains, which is needed to interact with many of Mailgun's APIs.

- Access: Given an email address as an identifier in the `src/mailgunDatapoints.ts` file, return a list of email lists the person is in.
- Erasure: Given an identifier and context, remove that person from Mailgun mailing lists.
- Seed: Given an identifier as a seed input, add them to the Mailgun organisation.

### Evaluation Criteria

We will evaluate your solution using the following rubric:
| Criteria | Below Expectations | Meets Expectation | Exceeds Expectations |
| ----------- | ----------- | ----------- | ----------- |
| Completeness | Basic functionality does not work, and/or has many bugs. | Implements the basic functionality without bugs. | Implements the basic functionality and at least one of the bonus challenges. |
| Readability & Maintainability | Inconsistent syntax (ie did not use a linter). Poor function/variable names. | Used a linter. Easy to understand function/variable names. | Follows best practices for writing React components. Modularized code. Leaves comments explaining non-obvious trade-offs/future breakage. |
| Robustness | Has no error handling, logging, etc. | Has some error handling and logging (or at least comments about TODOs). | All code paths have some error handling. Care has been taken to log errors and information that would help with future debugging. Tests are written. |
