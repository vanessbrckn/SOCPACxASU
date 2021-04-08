using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using DashboardApp.dbclasses;

namespace DashboardResults
{
    public partial class Results : Form
    {
        public Results()
        {
            InitializeComponent();

            placeLbl.Text = DashboardApp.dbclasses.helper.GetLocation(//locationID from DB Search)
        }
    }
}
