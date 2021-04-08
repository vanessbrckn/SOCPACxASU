using System;
using System.Collections.Generic;
using System.Text;
using Dapper; 

namespace DashboardApp.dbclasses
{
    public class airport
    {
        public int aid { get; set; }
        public int capacity { get; set; }
        public string location { get; set; }

    }
}
