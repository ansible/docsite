# Ansible user journey maps

This document extends Ansible personas by identifying and describing their major steps on user automation journeys.

Ansible community personas: https://hackmd.io/pZb5w5JFRQW3RJ73n23tlw?both#/

## Novice

```mermaid
journey
    title Novice journeys
    section Learn the basics
      Understand the fundamentals of Ansible automation: 5: Novice
      Install the Ansible package and run a hello world playbook: 5:
    section Explore the Ansible package
      Create a virtual environment: 5: Novice
      Install additional Ansible dev tools: 5: Novice
```

## User

```mermaid
journey
    title User journeys
    section Write playbooks
      How do I make my automation consistent?: 5:
      How do I make things reusable?: 5:
      How do I organize my project as my automation grows?: 5:
        How do I use roles to structure my project?: 3:
    section Run playbooks
      How do I use an execution environment?: 5:
      How do I use the AWX REST API?: 5:
      How do I use the AWX Web UI?: 5:
    section Share automation
      How do I create a collection?: 5:
      How do I allow others to run my playbook?: 5:
    section Have something to automate
      SRE process: 5:
      Raspberry pi cluster: 5:
      Network devices: 5:
```

### Beginner tasks

- Installs and/or updates ansible or ansible-core
- Installs or updates individual collections
- Creates and tests playbooks
- Creates inventories
- Tests, publishes, and maintains all of these

### Intermediate tasks

- Creates roles
- Creates job templates (for AWX users)
- Uses event-driven automation (ansible-rulebook - new)
- Contributes to collections (bugfixes, modules etc)
- Tests, publishes, and maintains all of these

### Advanced tasks

- Creates collections (reusable plugins, roles, and playbooks)
- Creates execution environments (collections, libraries, and ansible-core version)
- Tests, publishes, and maintains all of these


## Operations

## Developer

## Community maintainer

## Community member

## Community evangelist