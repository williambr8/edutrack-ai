// Add Subjects record
query subjects verb=POST {
  api_group = "edutrack-ai"

  input {
    dblink {
      table = "Subjects"
    }
  }

  stack {
    db.add Subjects {
      data = {created_at: "now"}
    } as $subjects
  }

  response = $subjects
}