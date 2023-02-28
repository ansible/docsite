# Ansible user journey maps

This document extends Ansible docsite personas by identifying and describing their automation journeys.

[Ansible docsite personas](https://github.com/ansible/docsite/blob/personas/personas/ansible-docsite-personas.md)

## Intro

Each persona has specific milestones in their automation journey.
And each milestone has specific major actions that the persona achieves.

```yaml
Milestone: Become aware
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

```yaml
Milestone: Learn the basics
  Understand the challenges of modern infrastructure management [content gap]
  Understand the fundamentals of Ansible automation
Milestone: Set up an automation project
  Install the Ansible package
  Create a basic inventory file
  Run an ad-hoc command
Milestone: Write first playbook
  Create a hello world playbook
  Run the playbook with the ansible-playbook command
```

## User

```yaml
Milestone: Have something to automate
  Start writing playbooks
  Evaluate plugins to see if results of execution meet needs
Milestone: Learn inventories
  Create an inventory file to manage multiple hosts
  Use dynamic inventories
Milestone: Organize the automation project as it starts to grow
  Use roles to structure the automation project
Milestone: Improve automation content
  Install developer tools (ansible-lint, vscode extension, molecule)
Milestone: Re-use existing automation content
  Start exploring Ansible Galaxy
  Install and use roles and/or collections
  Customize automation content
Milestone: Share automation content
  Submit roles to an existing collection
  Create a collection and upload to Galaxy
Milestone: Use AWX for more convenient automation
  Execute automation jobs on demand with the REST API or Web UI
  Schedule automation jobs
  Create AWX job templates
Milestone: Use Ansible Runner as an interface for automation
  Build execution environment with specific dependencies
  Use execution environments with AWX jobs
```

## Operations

```yaml
Milestone: Perform updates in production environments
  Check the porting guides.
Milestone: Administer Galaxy instance
Milestone: Administer AWX
  Control which EEs to use with automation jobs, where they run, and who can execute them
```

## Developer

```yaml
Milestone: Learn how to contribute code
  Review code of conduct and contributor guidelines
  Review PRs in an Ansible project
  Fix issues in an Ansible project, collection, or module
Milestone: Add to existing collection
  Include a new module
  Deprecate a module
Milestone: Convert role to collection
Milestone: Create a new collection
  Troubleshoot collections with ansible-navigator
  Request a collection be added to the Ansible package
Milestone: Use event-driven automation
```

## Community maintainer

```yaml
Milestone: Actively participate in the Ansible community
  Follow community-related discussions and participate in decisions
Milestone: Manage the Ansible project
  Ensure important issues are fixed
  Release project/collections regularly
  Oversee CI workflows, PR reviews and merges
Milestone: Foster community of contributors
```

## Community member

```yaml
Milestone: Become interested in joining the community
  Learn about the Ansible community and its purpose
  Review and agree to the code of conduct
  Join or initiate a discussion
  Participate in a meetup or other local event
  Contribute to an Ansible project
Milestone: Expand Ansible community activities
  Present at a meetup
  Write and share blog post/video etc
  Contribute a feature/collection etc to an Ansible project
Milestone: Become an Ansible community evangelist
  Host Ansible meetups
  Become a maintainer of an Ansible project or collection
  Become a member of Ansible steering committee
```