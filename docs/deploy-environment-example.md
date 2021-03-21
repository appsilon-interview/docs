# Deploy Environment Example

## Building Application

Prior to deploying application into AWS, Docker image should be built first. To build the image,
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

After image is built, you will need to push it to the DockerHub. To do so, log into DockerHub first:

``` {.sh}
$ export DOCKER_PASSWORD=<your dockerhub password>
$ export DOCKER_USERNAME=<your dockerhub username>
$ echo "${DOCKER_PASSWORD}" | docker login --username "$DOCKER_USERNAME" --password-stdin
```

Tag and push image:
``` {.sh}
$ make publish
```

## Deploying Infrastructure

In order to deploy a staging environment with all required AWS components, a dedicated [terraform](https://www.terraform.io/) module was created. 

For detailed explanation of AWS components used and their respective Terraform resources, please see module's respective [README](https://github.com/appsilon-interview/terraform/blob/master/modules/terraform-aws-appsilon/README.md) page.


### Dependencies

The following is required to be installed on your system:

-   terraform
-   awscli

### Deployment

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

Copy [example.tfvars](https://github.com/appsilon-interview/terraform/blob/master/example.tfvars)
to `terraform.tfvars` and using your favourite editor, update values
to suit your needs.


``` {.sh}
$ vim terraform.tfvars
region               = "eu-west-2"
domain               = "kloud-native.net"
appsilon_subdomain   = "rshiny"
rds_username         = appsilon-user
rds_password         = sup3rs3cr3tpw
rds_db_name          = "appsilon-db"
rds_instance         = "db.t2.micro"
appsilon_version_tag = "c9a417a"
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

Wait for ECS task to be provisioned and head down to `https://<your subdomain>.<domain>` to verify
the application had been deployed and is reachable.


## Cleaning Up
Run `terraform destroy` to destroy your existing resources:

``` {.sh}
$ terraform destroy -auto-aprove
```
[![asciicast](https://asciinema.org/a/400799.svg)](https://asciinema.org/a/400799)
