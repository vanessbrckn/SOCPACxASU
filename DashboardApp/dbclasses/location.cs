using System;
using System.Collections.Generic;
using System.Text;

namespace DashboardApp.dbclasses
{
    public class location
    {
        public double coordinates { get; set; }
        public string countryName { get; set; }
        public string lid { get; set; }
        public string safetyLevel { get; set; }
        public string weather { get; set; }
    }
}
