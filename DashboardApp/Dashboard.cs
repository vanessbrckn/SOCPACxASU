using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

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

            string targetName = nameTxt.Text;
            string targetBranch = branchTxt.Text;
            string targetRank = rankTxt.Text;
            string targetCountry = countryTxt.Text;
            string targetLat = latTxt.Text;
            string targetLong = longTxt.Text;

            
        }
    }
}
