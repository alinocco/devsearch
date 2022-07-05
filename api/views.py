from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import ProjectSerializer
from projects.models import Project, Review, Tag


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(uuid=pk)
    serializer = ProjectSerializer(project, many=False)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reviewProject(request, pk):
    project = Project.objects.get(uuid=pk)
    profile = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        project=project,
        owner=profile,
    )

    review.vote = data['vote']
    review.comment = data['comment']
    review.save()

    project.get_vote_statistics

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def removeTag(request):
    tag = request.data['tag']
    project = request.data['project']

    tag = Tag.objects.get(uuid=tag)
    project = Project.objects.get(uuid=project)

    project.tags.remove(tag)

    return Response('Tag was deleted!')


@api_view(['POST'])
def addTag(request):
    tag = request.data['tag']
    project = request.data['project']

    tag, created = Tag.objects.get_or_create(name=tag)
    project = Project.objects.get(uuid=project)

    project.tags.add(tag)

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
