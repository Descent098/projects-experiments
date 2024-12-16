# Gofr experimenting

Tsting out the [Gofr Framework](https://gofr.dev/). So far some initial results:

- Quite slow compiling
- Quite slow requests/responses
- JSON 
  - 404's are JSON which is interesting
  - Routes that return normal strings will drop the string as a "data" key in the returned JSON
- Has some insane functionality
  - [CLI](https://github.com/gofr-dev/gofr/tree/development/examples/sample-cmd)
  - [Cronjobs](https://github.com/gofr-dev/gofr/tree/development/examples/using-cron-jobs)
  - [Migrations](https://github.com/gofr-dev/gofr/tree/development/examples/using-migrations)
  - [GRPC](https://github.com/gofr-dev/gofr/tree/development/examples/grpc-server) 
