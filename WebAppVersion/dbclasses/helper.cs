using System;
using System.Collections.Generic;
using System.Text;
using Dapper;
using System.Data;
using System.Configuration;
using System.Data.SqlClient;
using System.Linq;
using DashboardApp.dbclasses;

namespace DashboardApp.dbclasses
{
    public static class helper
    {
        /* public static string CnnVal(string name)
         {
             return ConfigurationManager.ConnectionStrings[name].ConnectionString;
         }*/

        public static List<ranklevel> GetRanklevels()
        {
            using (IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["peopleplacesplanes"].ConnectionString))
            {
                return db.Query<ranklevel>
                    ("Select * From ranklevel").ToList();
            }
        }
        public static location GetLocation(int id)
        {
            using (IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["peopleplacesplanes"].ConnectionString))
            {
                return db.Query<location>
                    ("Select * From location WHERE id = @id", new { id }).SingleOrDefault();
            }
        }
    }
    
}
