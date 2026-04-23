// Query all Subjects records
query subjects verb=GET {
  api_group = "edutrack-ai"

  input {
  }

  stack {
    db.query Subjects {
      return = {type: "list"}
    } as $subjects
  }

  response = $subjects
}