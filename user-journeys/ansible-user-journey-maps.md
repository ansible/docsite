# Ansible user journey maps

This document extends Ansible personas by identifying and describing their automation journey milestones.

Ansible community personas: https://github.com/ansible/docsite/blob/personas/personas/ansible-docsite-personas.md

## Novice

```yaml
Milestone: Learn the basics
  Understand principles of modern infrastructure management
  Understand the fundamentals of Ansible automation
Milestone: Set up an automation project
  Install the Ansible package
  Create a basic inventory file
  Run an Ad-Hoc command
  [Not sure if it's needed for novices] Create a Python virtual environment
  [Not sure if it's needed for novices] Install additional Ansible dev tools
```

## User

[Note: not sure but maybe the below can be put right at the second-layer page?]

```yaml
Milestone: Start writing playbooks
  Run your first playbook
  Learn about recommended tools for playbook quality (ansible-lint, handlers, etc)
  Start validating playbooks
Milestone: Make playbooks reusable
  Organize the automation project as it grows.
  Use roles to structure the automation project.
Milestone: Learn inventories
  Create an inventory file to manage multiple servers
  Use dynamic inventories
Milestone: Test your roles
  Use Ansible Molecule to improve role quality.
Milestone: Use Ansible Galaxy
  Install and use roles
  Install and use collections

Advanced (including operators' tasks):
--------------------------------------

Milestone: Create execution environment
Milestone: AWX
  Manage multiple playbooks, inventories, and jobs with AWX.
  Use the AWX REST API.
  Use the AWX Web UI.
Milestone: Stand up private Galaxy instance
Milestone: Share automation
  Contribute to collections.
  Create a collection and publish it on Galaxy.
  [What is it about?] Allow others to run the playbook.
  Create and share AWX job templates.
```

## Developer

[Note: it's project-specific]
[Will it be per particular project? because the below is ansible-core/collections focused at the moment but it can alsobe AWX developer, Molecule developer, etc.]

```yaml
Milestone: Learn how to contribute code
  Review code of conduct and contributor guidelines
  Review issues and PRs in an Ansible project
  Fix issues and implement new features in an Ansible project
  Write a new component (for example, a module or plugin)
Milestone: Add to existing collection
  [I would exclude it as it overlaps with the previous milestone a lot] Include a new module
  [I believe it's a maintainer's task] Deprecate a module
[Should this belong to User?] Milestone: Convert role to collection
Milestone: Test your changes
  Understand testing in Ansible
  Run Sanity tests
  Write integration tests
  Write unit tests
Milestone: Create a new collection
  Use the collection skeleton
  Use GitHub actions to set up testing workflows
  Troubleshoot collections with ansible-navigator
  Request a collection be added to the Ansible package
[What is it about?] Milestone: Use event-driven automation

[Should we add something about publishing collections on Galaxy?]
```

## Community maintainer

[Note: it's project-specific]

```yaml
Milestone: [It's IMO too abstract] Actively participate in the Ansible community
  [It's about top-level governance IMO] Follow community-related discussions and participate in decisions
Milestone: Manage the Ansible project
  Ensure important issues are fixed
  Release project/collections regularly
  Oversee CI workflows, PR reviews and merges
Milestone: Foster community of contributors

[Alternative proposal]
Milestone: Learn maintainer restopsibilities
  Use existing communication channels, create new channels
  Ensure CI is working and relevant
  Review, merge and backport changes
  Release the project
  Maintain good collection documentation

Milestone: Expand a project community

Milestone: [We could put something here about participating in higher-level / cross-project governance stuff]
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
