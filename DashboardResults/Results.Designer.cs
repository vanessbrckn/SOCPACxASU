namespace DashboardResults
{
    partial class Results
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Results));
            this.peopleLbl = new System.Windows.Forms.Label();
            this.placeLbl = new System.Windows.Forms.Label();
            this.planesLbl = new System.Windows.Forms.Label();
            this.map = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.map)).BeginInit();
            this.SuspendLayout();
            // 
            // placeLbl
            // 
            this.placeLbl.AccessibleRole = System.Windows.Forms.AccessibleRole.None;
            this.placeLbl.AutoSize = true;
            this.placeLbl.Font = new System.Drawing.Font("Arial", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.placeLbl.Location = new System.Drawing.Point(77, 151);
            this.placeLbl.Name = "placeLbl";
            this.placeLbl.Size = new System.Drawing.Size(72, 22);
            this.placeLbl.TabIndex = 0;
            this.placeLbl.Text = "Places";
            // 
            // planesLbl
            // 
            this.planesLbl.AccessibleRole = System.Windows.Forms.AccessibleRole.None;
            this.planesLbl.AutoSize = true;
            this.planesLbl.Font = new System.Drawing.Font("Arial", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.planesLbl.Location = new System.Drawing.Point(77, 205);
            this.planesLbl.Name = "planesLbl";
            this.planesLbl.Size = new System.Drawing.Size(73, 22);
            this.planesLbl.TabIndex = 0;
            this.planesLbl.Text = "Planes";
            // 
            // map
            // 
            this.map.InitialImage = ((System.Drawing.Image)(resources.GetObject("map.InitialImage")));
            this.map.Location = new System.Drawing.Point(267, 46);
            this.map.Name = "map";
            this.map.Size = new System.Drawing.Size(489, 338);
            this.map.TabIndex = 1;
            this.map.TabStop = false;
            // 
            // Results
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.map);
            this.Controls.Add(this.planesLbl);
            this.Controls.Add(this.placeLbl);
            this.Controls.Add(this.peopleLbl);
            this.Name = "Results";
            this.Text = "Results";
            ((System.ComponentModel.ISupportInitialize)(this.map)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label peopleLbl;
        private System.Windows.Forms.Label placeLbl;
        private System.Windows.Forms.Label planesLbl;
        private System.Windows.Forms.PictureBox map;
    }
}

