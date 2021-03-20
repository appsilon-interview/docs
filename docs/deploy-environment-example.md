Deploy Environment Example
===========================

Building Application Docker Image
--------------------------------

Prior to deploying application, Docker image should be built first. To build the image,
clone the repository:

``` {.sh}
$ git clone git@github.com:appsilon-interview/app.git
$ cd app
```

And run:

``` {.sh}
$ make build
```

[![asciicast](https://asciinema.org/a/400482.svg)](https://asciinema.org/a/400482)

To push image to DockerHub, you'll need to log into DockerHub first:

``` {.sh}
$ export DOCKER_PASSWORD=<your dockerhub password>
$ export DOCKER_USERNAME=<your dockerhub username>
$ echo "${DOCKER_PASSWORD}" | docker login --username "$DOCKER_USERNAME" --password-stdin
```

Tag and push image:
``` {.sh}
$ make publish
```

Deploying infrastructure
--------------------------------

A [terraform](https://www.terraform.io/) module to deploy a secure,
functional staging environment on [AWS](http://aws.amazon.com/).

Dependencies
------------

The following is required to be installed on your system:

-   terraform
-   awscli

Deployment
----------

To deploy infrastructure, clone the repository:

``` {.sh}
$ git clone git@github.com:appsilon-interview/terraform.git
$ cd terraform
```

Configure your access and secret key within `awscli`, specifying region and default
output:

``` {.sh}
$ aws configure
```

Using your favourite editor, update values in [terraform.tfvars](https://github.com/appsilon-interview/terraform/blob/master/terraform.tfvars)
to suit your needs.


``` {.sh}
$ vim terraform.tfvars
region               = "eu-west-2"
domain               = "kloud-native.net"
appsilon_subdomain   = <subdomain for your application>
rds_username         = <database username>
rds_password         = <database password>
rds_db_name          = "<database name>
rds_instance         = "db.t2.micro"
appsilon_version_tag = <docker tag of your built image>
```

Run `terraform init` to initalize modules:

``` {.sh}
$ terraform init
```

Run `terraform plan` to view changes terraform will make:
``` {.sh}
$ terraform plan
```
[![asciicast](https://asciinema.org/a/400798.svg)](https://asciinema.org/a/400798)


Run `terraform apply` to create your resources:

``` {.sh}
$ terraform apply -auto-approve
```
[![asciicast](https://asciinema.org/a/400796.svg)](https://asciinema.org/a/400796)


Run `terraform destroy` to destroy your resources:

``` {.sh}
$ terraform destroy -auto-aprove
```
[![asciicast](https://asciinema.org/a/400799.svg)](https://asciinema.org/a/400799)
