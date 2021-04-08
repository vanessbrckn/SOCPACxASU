using System;
using System.Collections.Generic;
using System.Text;
using System.Data;
using System.Configuration;
using Dapper;

namespace DashboardApp.dbclasses
{
    public class ranklevel
    {
        public string bid { get; set; }
        public string insMark { get; set; }
        public int rank_level { get; set; }
        public string rid { get; set; }
        public string titel { get; set; }

    }
}
