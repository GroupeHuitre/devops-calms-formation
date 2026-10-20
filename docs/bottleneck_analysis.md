# Bottleneck Analysis and Value Stream Mapping - NovaTech

This document synthesizes the identified bottlenecks at **Novatech**, categorized by major operational domains, along with a Value Stream Mapping analysis.

## 1. Bottlenecks Categorized by Domain

### Governance, Organization & Planning

* **Lack of visibility and task prioritization:** Inadequate tracking systems; need to introduce a Kanban board supported by key rituals (Daily Standups, Weekly Meetings, Copil task allocation).

* **Unclear roles & responsibilities:** Absence of a RACI matrix to define ownership across departments and teams.

* **Issue tracking:** Missing a tagging system to efficiently route issues to the appropriate teams.

* **Release planning:** Lack of a defined release and deployment calendar.

### Development Process & Code Reviews

* **Unstandardized contributions:** Need for a dedicated Pull Request (PR) template to speed up reviews and minimize back-and-forth communication.

* **Batch sizes too large:** Monolithic updates increase failure risks; adopting atomic commits will enable smaller, incremental deliverables.

### Quality, Security & CI/CD

* **Slow and manual deployments:** Manual deployment steps without an automated CI/CD pipeline.

* **Insufficient quality and security controls:** Absence of automated security scans (GA Trivy, Gitleaks, Trufflehog, SonarQube for code quality, Blackduck for SBOM).

* **Missing Quality Gates:** Lack of mandatory security and quality gate checks prior to PR approvals and merges.

### Infrastructure, Testing & Operations

* **Test environment issues:** Unshared or inconsistent environments; requirement for a Docker-based test environment (mini cross-OS platform engineering approach).

* **Production deployment rules:** Strict rule against Friday/late-day deployments to reduce the need for on-call engineers; mandatory feature validation on staging/test environments first.

* **Observability and resilience:** Absence of centralized monitoring (Prometheus / Grafana for server metrics and logs) and automated backup solutions (DB replication, volume backups).

* **Infrastructure management:** Lack of global visibility over infrastructure configurations; adoption of Infrastructure as Code (IaC using Terraform) combined with Ansible for provisioning and automated routines.

## 2. Value Stream Mapping (VSM)

The following matrix breaks down each phase of the delivery lifecycle, highlighting active effort hours, wait times, and actionable hypotheses to verify:

| Stage | Active Time (Hours) | Wait Time (Hours) | Hypothesis to Verify / Improvement Action |
| ----- | ----- | ----- | ----- |
| **Specification** | 2h | 6h | **Prioritization & Definition of Done delay:** Implement Daily Standups and Weekly Copil meetings to clarify, prioritize, and assign tasks before development starts. |
| **Development** | 12h | 4h | **Code review wait time:** Delivery of smaller, incremental changes using atomic commits. |
| **Code Review** | 2h | 10h | **Reviewer availability:** Introduce structured PR templates, automate unit and critical E2E tests, and enforce test pass conditions as quality gates with high coverage targets. |
| **Testing** | 3h | 24h | **Unshared test environments:** Standardize environments using Docker containerization (cross-OS compatibility) and dedicated staging servers. |
| **Change Validation** | 1h | 36h | **Large-batch validations:** Define changes in time-boxed sprints/tasks. Move away from large batches toward frequent, smaller releases (ship small, fail fast, iterate quickly). |
| **Deployment** | 2h | 8h | **Deployment window restrictions:** Automate via CI/CD pipelines and leverage IaC for fast, repeatable deployments. |
