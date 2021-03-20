Getting Started
===============

This project serves as a fully working and tested solution for deploying
staging environment for R-Shiny application into AWS. 

Technologies used
-----------------

**Terraform**[^1] is used to provision infrastructure resources like
VPC, compute instances, DNS records, RDS instance and many more.

**AWS**[^3] public cloud is used as a Cloud provider of choice.

**R-Shiny**[^5] is used as a framework to deploy an example application.

All Docker images are stored in public **DockerHub**[^6] registry.

Entire source code is stored in **GitHub**'s
[appsilon-interview](https://github.com/appsilon-interview) organisation.

**GitHub Actions**[^7] are used for continuous integration, running
tests, building application's Docker image, linting and static validation of 
IaaC code for potential security issues.

[^1]: [Use Infrastructure as Code to provision and manage any cloud,
    infrastructure, or service.](https://www.terraform.io/)

[^3]: [The Amazon AWS offers you a large number of cloud
    solutions that are billed on a pay-as-you-go
    basis.](https://aws.amazon.com/)

[^5]: [Shiny is an R package that makes it easy to build interactive web apps 
    straight from R.](https://shiny.rstudio.com/)

[^6]: [Storing and distribution system for named Docker
    images.](https://hub.docker.com/)

[^7]: [GitHub Actions enables you to create custom software development
    life cycle (SDLC) workflows directly in your GitHub
    repository.](https://docs.github.com/en/actions)

