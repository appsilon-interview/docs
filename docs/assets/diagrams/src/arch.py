from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.management import Cloudwatch
from diagrams.aws.general import InternetGateway
from diagrams.aws.security import CertificateManager, IAM
from diagrams.aws.general import Users
from diagrams.aws.storage import S3

with Diagram("Architecture", show=False):

    cw = Cloudwatch("Cloudwatch")
    s3 = S3("S3")
    users = Users("Users")
    iam = IAM("IAM")
    dns = Route53("DNS")
    cm = CertificateManager("CertificateManager")
    listener = InternetGateway(":443")

    with Cluster("VPC: 172.16.x.x"):
        lb = ELB("ALB")

        with Cluster("ECS"):
            with Cluster("Public Subnet #1"):
                ecs_stack_1 = ECS("rshiny-app-1")

            with Cluster("Public Subnet #2"):
                ecs_stack_2 = ECS("rshiny-app-2")


        with Cluster("Private Subnet #1"):
            with Cluster("RDS Cluster"):
                db_1 = RDS("postgresql db")

    users << dns >> lb
    users >> listener >> lb
    lb >> Edge(label=":8080") >> ecs_stack_1
    lb >> Edge(label=":8080") >> ecs_stack_2
    ecs_stack_1 >> Edge(label=":5432") >> db_1
    ecs_stack_2 >> Edge(label=":5432") >> db_1
    db_1 << cw
    ecs_stack_1 << cw
    ecs_stack_2 << cw
    cm << Edge(label="Use certificate") << lb
    lb >> s3
    iam - Edge(style="dashed") - ecs_stack_1
    iam - Edge(style="dashed") - s3
