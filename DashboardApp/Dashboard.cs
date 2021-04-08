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

            Address addr = client.QueryAddress($"{targetCity} {targetCountry}");



            //Geolocation.Coordinate coordinate = new Geolocation.Coordinate();
            //string targetLat = coordinate.Latitude.ToString();
            //string targetLong = coordinate.Longitude.ToString();

            latLbl.Text = addr.State.ToString();
            longLbl.Text = addr.Longitude.ToString();

            

            
            
        }
    }
}
