using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Device.Location;
using System.Threading;

namespace Proto
{
    public partial class Dashboard : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            TextBox4.Text = "";
            TextBox5.Text = "";

            GeoCoordinateWatcher watcher = new GeoCoordinateWatcher();

            bool started = watcher.TryStart(false, TimeSpan.FromMilliseconds(2000));
            if (!started)
            {
                Label1.Text = "Error Starting Location Services";
            }

            Thread.Sleep(500);

            if (watcher.Status == GeoPositionStatus.Ready)
            {
                TextBox4.Text = watcher.Position.Location.Latitude.ToString();
                TextBox5.Text = watcher.Position.Location.Longitude.ToString();
            }
            else if (watcher.Status == GeoPositionStatus.NoData)
                Label1.Text = "Location Services Are Currently Disabled";
        }
    }
}