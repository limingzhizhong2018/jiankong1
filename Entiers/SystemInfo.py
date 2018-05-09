class SystemInfo(object):

    def systemInfo(self, memLoad, memUsed, memTotal):
        self.mem_load = [
            {
                "measurement": "mem_load_short",
                "tags":
                    {
                        "host": "server01"
                    },
                "fields":
                    {
                        "value": memLoad,
                        "success": 1,
                    }
            }
        ]
        self.mem_used = [
            {
                 "measurement": "mem_used_hort",
                 "tags":
                    {
                        "host": "server01"
                    },
                 "fields":
                     {
                        "value": memUsed,
                        "success": 1,
                     }
            }
        ]
        self. mem_total = [
        {
            "measurement": "mem_total_short",
            "tags":
                {
                    "host": "server01"
                },
            "fields":
                {
                    "value": memTotal,
                    "success": 1,
                }
        }
       ]
