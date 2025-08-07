## ✅ Terraform Challenge 4 – IAM Data Sources, Outputs & Dynamic User Creation

### 🎯 Goal:

1. Fetch and list all IAM users in the AWS account.
2. Output the **count** of total IAM users.
3. Create a new IAM user with a dynamic name in the format: `admin-user<account_id>`.

---

### 🔨 Key Terraform Concepts Used:

| Concept                    | Description                                                        |
| -------------------------- | ------------------------------------------------------------------ |
| `data.aws_iam_users`       | Fetches all IAM users from your AWS account                        |
| `data.aws_caller_identity` | Retrieves AWS account metadata (account\_id, user\_id, ARN)        |
| `output`                   | Used to display usernames and total count                          |
| `length()` function        | Calculates the number of elements in a list (used for total users) |
| Interpolation (`${}`)      | Dynamically inserts account ID into IAM username and tag           |

---

### 🧩 Code Breakdown:

```hcl
provider "aws" {
  region = "eu-west-2"
}

# ✅ 1. Fetch all IAM users
data "aws_iam_users" "users" {}

# ✅ 2. Fetch AWS Account ID for dynamic naming
data "aws_caller_identity" "current" {}

# ✅ 3. Create an IAM user with a dynamic name using account ID
resource "aws_iam_user" "lb" {
  name = "admin-user${data.aws_caller_identity.current.account_id}"
  path = "/system/"

  tags = {
    name = "admin-user${data.aws_caller_identity.current.account_id}"
  }
}

# ✅ 4. Output list of usernames
output "user-names" {
  value = data.aws_iam_users.users.names
}

# ✅ 5. Output total number of IAM users
output "total_users" {
  value = length(data.aws_iam_users.users.names)
}

# ✅ 6. Output AWS account ID (optional for debugging)
output "account_id" {
  value = data.aws_caller_identity.current.account_id
}
```

---

### 🧠 What You Learned:

| Feature                 | Real-World Use                                                           |
| ----------------------- | ------------------------------------------------------------------------ |
| `aws_iam_users`         | Useful for audits, access management, and visibility                     |
| `aws_caller_identity`   | Great for tagging, naming conventions, or resource filtering per account |
| Output values           | Essential for debugging, chaining modules, or documentation              |
| `length()`              | A basic but powerful function to handle lists or maps                    |
| Dynamic resource naming | Helps in multi-account automation and uniqueness                         |

---

### 🧪 Validation Steps:

1. `terraform init`
2. `terraform plan` – Confirm IAM user creation, list of users, and count.
3. `terraform apply -auto-approve` – Execute creation.
4. Verify:

   * New user appears in **IAM console** with correct dynamic name.
   * Output shows accurate user count and names.

---

### 🧼 Cleanup:

```bash
terraform destroy -auto-approve
```

> Avoid lingering IAM users or sensitive resources if not needed. Stay within free-tier limits!
