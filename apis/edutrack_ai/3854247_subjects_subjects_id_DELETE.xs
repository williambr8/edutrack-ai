// Delete Subjects record.
query "subjects/{subjects_id}" verb=DELETE {
  api_group = "edutrack-ai"

  input {
    int subjects_id? filters=min:1
  }

  stack {
    db.del Subjects {
      field_name = "id"
      field_value = $input.subjects_id
    }
  }

  response = null
}