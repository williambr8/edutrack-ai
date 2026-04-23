// Edit Subjects record
query "subjects/{subjects_id}" verb=PATCH {
  api_group = "edutrack-ai"

  input {
    int subjects_id? filters=min:1
    dblink {
      table = "Subjects"
    }
  }

  stack {
    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input
  
    db.patch Subjects {
      field_name = "id"
      field_value = $input.subjects_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $subjects
  }

  response = $subjects
}