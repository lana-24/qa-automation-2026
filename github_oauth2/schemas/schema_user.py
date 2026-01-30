import jsonschema
from typing import Literal

def user_schema(data: dict,schema_name:
                Literal['user',
                        'users',
                        'hovecard',
                        'list_email',
                        'ssh',
                        'public_ssh',
                        'list_ssh']
                ):
    schemas = {
        "user" : {"type" : "object",
                  "properties" : {"login" : {"type" : ["string","null"]},
                                  "id" : {"type" : "integer"},
                                  "url" : {"type" : ["string","null"]},
                                  "name" : {"type" : ["string","null"]},
                                  "bio" : {"type" : ["string","null"]},
                                  "created_at" : {"type" : ["string","null"]}
                        },
                  "required" : ["login","id","name","created_at"]},
        
        "users" : {"type" : "array",
                   "items" : {"properties" : {"login" : {"type" : "string"},
                                            "id" : {"type" : "integer"},
                                            "url" : {"type" : "string"},
                                            "name" : {"type" : "string"},
                                            "bio" : {"type" : "string"},
                                            "created_at" : {"type" : "string"}
                                              }},
                   "required" : ["login","id","name","created_at"]
                   },
        "list_email" :  {"type" : "array",
                         "items" : {"properties" : {"email" : {"type": ["string","null"]},
                                                    "verified" : {"type" : "boolean"},
                                                    "primary" : {"type" : "boolean"},
                                                    "visibility" : {"type" : ["string","null"]}
                                              }},
                          "required" : ["email","verified","primary","visibility"]
                          },
        
        "ssh" : {"type" : "object",
                  "properties" : {"key" : {"type" : "string"},
                                  "id" : {"type" : "integer"},
                                  "url" : {"type" : "string"},
                                  "title" : {"type" : "string"},
                                  "created_at" : {"type" : "string"}
                                  
                                  },
                 "required" : ["key","id","title","created_at"]
                 },
        
        "public_ssh" :  {"type" : "array",
                         "items" : { "properties" : {"id" : {"type" : "integer"},
                                                     "key" : {"type" : "string"}
                                                     }
                                    },
                         "required" : ["id","key"]
                         },
        
        "list_ssh" : {"type" : "array",
                      "items" : {"properties" : {"key" : {"type" : "string"},
                                                "id" : {"type" : "integer"},
                                                "url" : {"type" : "string"},
                                                "title" : {"type" : "string"},
                                                "created_at" : {"type" : "string"}
                                              }},
                      "required" : ["key","id","title","created_at"]
                      }
}
    schema = schemas.get(schema_name)
    jsonschema.validate(data , schema)
