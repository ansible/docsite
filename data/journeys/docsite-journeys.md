# Ansible user journey maps

This document extends Ansible docsite personas by identifying and describing their automation journeys.

[Ansible docsite personas](docsite-personas.md)

## Intro

Each persona has specific milestones in their automation journey.
And each milestone has specific major actions that the persona achieves.
The first milestone of each journey starts with human motivation.

```yaml
Milestone: Aware
  Major action
  Major action
  ...
Milestone: Evaluate
  Major action
  Major action
  ...
Milestone: Adopt
  Major action
  Major action
  ...
Milestone: Scale
  Major action
  Major action
  ...
```

## Novice

Get started with Ansible box content.

```yaml
Milestone: Need to learn the basics
  Understand the challenges of modern infrastructure management [content gap]
  Understand the fundamentals of Ansible automation

Milestone: Set up an automation project
  Install the Ansible package
  Run your first ad hoc command in a few easy steps
```

## Users

```yaml
Milestone: Create automation
  Start writing Ansible playbooks
  Learn about Ansible modules

Milestone: Learn inventories
  Build inventory files to manage multiple hosts
  Use dynamic inventories

Milestone: Organize automation projects
  Use roles to structure the automation project

Milestone: Use Ansible tooling
  Use Ansible Lint to validate playbooks
  Install Molecule to develop and test Ansible roles
  Create and test playbooks with Ansible Navigator
  Use Ansible with Visual Studio Code and OpenVSX compatible editors

Milestone: Find Automation content
  Start exploring Ansible Galaxy
  Install and use roles
  Install and use collections

Milestone: Share automation content
  Submit roles to an existing collection
  Create a new collection
  Upload a collection to Ansible Galaxy

Milestone: Schedule and run automation jobs [TODO Add AWX overview, API]
  Execute automation jobs on demand
  Schedule automation jobs

Milestone: Embed automation in systems
  Build execution environment with specific dependencies
  Use execution environments with AWX jobs
```

## Developers

```yaml
Milestone: Start writing code
  Set up your development environment
  Learn how Ansible works
  Write custom modules or plugins

Milestone: Contribute code to a collection
  Make your first contribution
  Explore Collection contributor guide
  Contribute your module to an existing collection
  Review the lifecycle of an Ansible module or plugin

Milestone: Test plugins and modules
  Understand testing in Ansible
  Run sanity tests
  Write integration tests
  Write unit tests

Milestone: Create new collections
  Set things up with the collection skeleton
  Test your collection for code quality
  Publish your collection on a distribution server
  Request a collection be added to the Ansible package
```

## Maintainers

```yaml
Milestone: Learn about community maintainer responsibilities
  Review community maintainer responsibilities
  Backport merged pull requests to stable branches
  Regularly release stable versions
  Look after collection documentation

Milestone: Expand community around a collection
  Explore ways to grow community
  Maintain good contributor documentation
  Understand Ansible contributor paths

Milestone: Get collections included in the Ansible package
  Understand the inclusion process
  Review other inclusion requests
  Submit your collection for inclusion

Milestone: Participate in cross-project governance
  Discuss and vote on community topics
  Join the Ansible community steering committee
```

## Community member

TODO Decide whether we want to have this or we can just redirect visitors
to the new community website

```yaml
Milestone: Become interested in joining the community
  Learn about the Ansible community and its purpose
  Review and agree to the code of conduct
  Join or initiate a discussion
Milestone: Start actively participating in the Ansible community
  Participate in a meetup or other local event
  Contribute to an Ansible project
Milestone: Expand Ansible community activities
  Present at a meetup
  Write and share blog post or YouTube video, etc.
Milestone: Become an Ansible community evangelist
  Host an Ansible meetup
  Become a maintainer of an Ansible project or collection
  Join the Ansible steering committee
```
