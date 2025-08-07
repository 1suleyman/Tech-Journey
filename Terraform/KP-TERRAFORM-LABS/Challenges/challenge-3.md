# ✅ Terraform Challenge 3 – Dynamic EC2 Instances with `for_each`

### 🧠 Goal:

Use the `for_each` loop in Terraform to dynamically create multiple EC2 instances from a `map` variable, such that:

* A new instance is created for each key-value pair in the map
* If a key is removed, the instance is destroyed
* If a key is added, a new instance is created
* If a value is updated (e.g. instance type), the instance is modified

---

## 🗂️ Folder Structure:

| File           | Purpose                                           |
| -------------- | ------------------------------------------------- |
| `main.tf`      | Defines the dynamic EC2 resource using `for_each` |
| `variables.tf` | Declares the map variable `instance_config`       |

---

## 🧾 Terraform Files:

### 🔹 `variables.tf`

```hcl
variable "instance_config" {
  type = map(object({
    instance_type = string
    ami           = string
  }))
  default = {
    instance1 = { instance_type = "t2.micro", ami = "ami-03a6eaae9938c858c" }
    instance2 = { instance_type = "t2.small", ami = "ami-053b0d53c279acc90" }
  }
}
```

### 🔹 `main.tf`

```hcl
resource "aws_instance" "multiple_ec2" {
  for_each = var.instance_config

  ami           = each.value.ami
  instance_type = each.value.instance_type

  tags = {
    Name = each.key
  }
}
```

---

## 🔁 How `for_each` Works Here:

| Term                       | Meaning                                  |
| -------------------------- | ---------------------------------------- |
| `for_each`                 | Loops through each key in the map        |
| `each.key`                 | Name of the instance (e.g., `instance1`) |
| `each.value.ami`           | AMI value from the map                   |
| `each.value.instance_type` | Instance type from the map               |

Example:

```hcl
instance1 = { instance_type = "t2.micro", ami = "ami-123" }
```

Creates an instance with type `t2.micro` and AMI `ami-123`.

---

## 🧪 Demo Scenarios & Behavior

### ✅ Add a New Instance

Add this to `instance_config`:

```hcl
instance3 = { instance_type = "t2.nano", ami = "ami-0abc1234567890" }
```

→ `terraform apply` will **create** a new instance.

---

### ❌ Remove an Instance

Remove `instance2` from the map.

→ `terraform apply` will **destroy** `instance2`.

---

### 🔁 Modify an Instance

Change `instance_type` of `instance1`:

```hcl
instance1 = { instance_type = "t2.small", ami = "ami-03a6eaae9938c858c" }
```

→ `terraform apply` will **modify** the instance in-place.

---

## 🔍 .tfstate View

* Instance keys show up as part of the resource name:

  ```
  aws_instance.multiple_ec2["instance1"]
  aws_instance.multiple_ec2["instance3"]
  ```

---

## ✅ Clean Up

Always run:

```bash
terraform destroy -auto-approve
```

To avoid AWS charges.

---

## 📚 Key Takeaways

| Concept            | Explanation                                                                    |
| ------------------ | ------------------------------------------------------------------------------ |
| `for_each`         | Lets you dynamically manage multiple resources based on map or set             |
| `each.key`         | Reference to the current item name (e.g., `instance1`)                         |
| `each.value`       | The object (e.g., `{ instance_type = "t2.micro", ami = "ami-123" }`)           |
| .tfstate tracking  | Resources are tracked with their key name to manage add/remove/update behavior |
| Real-world benefit | Avoids duplication, enables scaling, makes infra changes easy and safe         |

