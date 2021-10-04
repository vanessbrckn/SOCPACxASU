using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Geolocation;
using GoogleMapsClient;

namespace DashboardApp
{
    public partial class Dashboard : Form
    {
        public Dashboard()
        {
            InitializeComponent();
        }

        private void submitBtn_Click(object sender, EventArgs e)
        {
            GoogleMaps client = new GoogleMaps("AIzaSyAScSP2zdmi7mzAqW9Ow3Fi434Y45YqriI");

               
            string targetName = nameTxt.Text;
            string targetBranch = branchTxt.Text;
            string targetRank = rankTxt.Text;
            string targetCountry = countryTxt.Text;
            string targetCity = cityLbl.Text;

            //here is the connection string for our DB 
            //Database={your_database}; Data Source=socpacxasu.mysql.database.azure.com; User Id=capstoneAdmin@socpacxasu; Password={your_password}

            Address addr = client.QueryAddress($"{targetCity} {targetCountry}");



            //Geolocation.Coordinate coordinate = new Geolocation.Coordinate();
            //string targetLat = coordinate.Latitude.ToString();
            //string targetLong = coordinate.Longitude.ToString();

            latLbl.Text = addr.State.ToString();
            longLbl.Text = addr.Longitude.ToString();

            //need to find an API that returns coordinates to search with in DB

            
            
        }
    }
}
