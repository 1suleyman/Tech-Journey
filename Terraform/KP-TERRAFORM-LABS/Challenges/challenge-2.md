# ✅ Terraform Challenge 2 — Optimization & Debugging Practice

This challenge focuses on **optimizing and troubleshooting Terraform code** for real-world production readiness. The goal is to go beyond just "making it work" and ensure the code is maintainable, modular, and professional.

---

## 📌 Challenge Summary

You're given a working Terraform script that:

* Creates an **AWS Security Group** with 3 inbound rules and 1 outbound rule
* Creates an **Elastic IP (EIP)** resource
* Uses outdated syntax, hardcoded values, poor formatting, and lacks modular structure

Your task:
✅ **Fix errors**
✅ **Apply best practices**
✅ **Make it production-ready**

---

## 🧠 What You’ll Learn

| Concept                         | What You Did                                                                                 |
| ------------------------------- | -------------------------------------------------------------------------------------------- |
| 🔍 **Troubleshooting**          | Fixed misplaced `egress` block outside the resource                                          |
| 🔐 **Provider Version Control** | Used `terraform init -upgrade` to update provider version in `terraform.lock.hcl`            |
| 🎯 **Validation**               | Used `terraform validate` and `terraform plan` to catch and fix syntax and version issues    |
| 📦 **Variable Optimization**    | Moved hardcoded values (ports, CIDRs) to `variables.tf` and `terraform.tfvars`               |
| 🧽 **Code Formatting**          | Used `terraform fmt` to automatically format inconsistent indentation                        |
| 🏷️ **Tagging**                 | Added `tags` for resource ownership, team, and environment                                   |
| 📣 **Descriptions**             | Added `description` fields to each rule for better console visibility                        |
| 🔁 **Variable Precedence**      | Used `-var` to override values from the CLI (e.g., `splunk = 8089`)                          |
| 🗂️ **Modular Structure**       | Split code into `providers.tf`, `variables.tf`, `sg.tf`, and `eip.tf`                        |
| 🛡️ **State Awareness**         | Understood how moving or renaming resources can trigger destruction unless handled carefully |

---

## 🔧 Final File Structure

```bash
terraform-challenge-2/
├── eip.tf                  # EIP resource
├── providers.tf            # AWS provider setup
├── sg.tf                   # Security Group resource
├── variables.tf            # All variable definitions
├── terraform.tfvars        # Actual variable values (e.g., ports, CIDRs)
├── terraform.lock.hcl      # Provider plugin versions (auto-managed)
```

---

## 📋 Example Variables

**variables.tf**

```hcl
variable "https" {}
variable "apis" {}
variable "prod_apis" {}
variable "dev_vpc" {}
variable "splunk" {
  default = 8088
}
```

**terraform.tfvars**

```hcl
https     = 443
apis      = 8080
prod_apis = 8443
dev_vpc   = "172.31.0.0/16"
```

---

## 🧪 CLI Commands Used

```bash
terraform init                   # Initialize Terraform directory
terraform init -upgrade         # Upgrade providers from lock file
terraform validate              # Validate syntax
terraform fmt sg.tf             # Format code properly
terraform plan                  # Preview changes
terraform apply -auto-approve   # Apply changes
terraform apply -var="splunk=8089" -auto-approve   # CLI override
terraform destroy -auto-approve # Clean up
```

---

## 🚨 Gotchas & Lessons

| Lesson                                        | Why It Matters                                                 |
| --------------------------------------------- | -------------------------------------------------------------- |
| Misplaced blocks (like `egress`) break code   | Terraform expects correct structure, else it fails             |
| `terraform.lock.hcl` pins provider versions   | Prevents silent upgrades; must upgrade intentionally           |
| Hardcoded values make refactoring painful     | Use variables to reduce duplication                            |
| Tags + Descriptions = operational visibility  | Helps teams manage, audit, and debug in real-world deployments |
| Modular files = easier collaboration          | Team members can edit only what they need                      |
| Renaming resource blocks triggers destruction | Always be careful with renames or refactoring resource labels  |

---

## 🧠 Final Thought

This challenge mimics real-life production scenarios where clean code, consistency, and infrastructure safety are critical. It’s not just about making Terraform **work** — it's about making it **sustainable**.
