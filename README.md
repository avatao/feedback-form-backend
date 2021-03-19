# Feedback form backend
Currently supported endpoints:
- /feedbacks

## Local usage
Just build the Docker image and run it:
1.  `docker build . -t mini-backend --no-cache`
2.  `docker run --rm -p 5000:5000 mini-backend`

## Authentication
The mini backend doesn't validate the JWTs and only checks the `user_id` key's value. Currently there are no separate roles, just authenticated users and guests.

Two seeded users:
- FirstUser:
  * Payload: {"user_id": "1"}
  * Token: `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMSJ9.VzqrIt7rU5JEQzVsgk-hxGr56VphfQF9h5KnpOhyYvk`
- SecondUser:
  * Payload: {"user_id": "2"}
  * Token: `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMiJ9.dvVCAT2exyaUMeJSFZh7ck0xrUcNqmrhjcje23tPiGE`

## API usage
Please check `openapi.yaml` for more information.

## License
Property of Avatao
