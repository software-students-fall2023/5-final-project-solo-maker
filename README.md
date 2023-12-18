# Final Project

An exercise to put to practice software development teamwork, subsystem communication, containers, deployment, and CI/CD pipelines. See [instructions](./instructions.md) for details.

# Note app + web crawler

We can take add/revise/delete notes with note title and Description in the Note app. Also, there is a web crawler integrated in the website called scapy to collect and visualized data for video website Bilibili(Chinese biggest video website, description below) 

note: The whole system is build on flask + jquery. Because I don't want to get annoyed by jquery environment. So I package my jquery build dictionary in the file.

## Badges

[![Docker Build and Deploy](https://github.com/software-students-fall2023/5-final-project-solo-maker/actions/workflows/deploy.yml/badge.svg)](https://github.com/software-students-fall2023/5-final-project-solo-maker/actions/workflows/deploy.yml)

[![note-App-test](https://github.com/software-students-fall2023/5-final-project-solo-maker/actions/workflows/note_app_test.yml/badge.svg)](https://github.com/software-students-fall2023/5-final-project-solo-maker/actions/workflows/note_app_test.yml)

[![scapy-backend-test](https://github.com/software-students-fall2023/5-final-project-solo-maker/actions/workflows/scapy_backend_test.yml/badge.svg)](https://github.com/software-students-fall2023/5-final-project-solo-maker/actions/workflows/scapy_backend_test.yml)

## Container Images

Below are the DockerHub links to the container images for each custom subsystem:

- **note-app**: [DockerHub Link](https://hub.docker.com/r/asukatan/note-app)
- **web crawler for bilibili**: [DockerHub Link](https://hub.docker.com/r/asukatan/scapy-backend)

## Teammates

Meet our team members:

- [Yuantian Tan](https://github.com/AsukaTan)

  Yes! Only myself:)

## Deployment

Go directly to this link

http://167.71.92.148:5000/

### Or

```
git clone https://github.com/software-students-fall2023/5-final-project-solo-maker
```

then build project

```
docker docker-compose up -d
```

Go to web

http://127.0.0.1:5000

# How to use

Note app is straight forward, which I will not introduce it.

## How to use web crawler

example usage: 

https://space.bilibili.com/1525355?spm_id_from=333.337.0.0 and find his UID 1525355

Make sure the content creator have Collection

Type UID into search box, and Get the result

## Testing crawler

provide UID for testing:

1525355

546195

15773384

## What is bilibili

**A.K.A** Chinese Youtube with millions users

the most popular video website in China

Bilibili (often referred to as 哔哩哔哩 or B Site) is one of Chi	na's most popular video sharing websites among young people. Founded in 2009, Bilibili initially started as a video sharing website focused on ACG (Animation, Comics, and Games) culture but has since expanded to include a wide variety of content, including lifestyle, technology, entertainment, and more.

### Website

[Bilibili Official Website](https://www.bilibili.com).

