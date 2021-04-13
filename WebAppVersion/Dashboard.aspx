<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Dashboard.aspx.cs" Inherits="Proto.Dashboard" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">

    .jumbotron {
        margin-top: 20px;
    }

    .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
  *,
  *:before,
  *:after {
    color: #000 !important;
    text-shadow: none !important;
    background: transparent !important;
    -webkit-box-shadow: none !important;
    box-shadow: none !important;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 63px;
  }
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
h1,
.h1 {
  font-size: 36px;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 20px;
  margin-bottom: 10px;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 21px;
  font-weight: 200;
}
  .lead {
    font-size: 21px;
  }
.lead {
  margin-bottom: 20px;
  font-size: 16px;
  font-weight: 300;
  line-height: 1.4;
}
p {
  margin: 0 0 10px;
}
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  input,
select,
textarea {
    max-width: 280px;
}


input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
input {
  line-height: normal;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
.row {
  margin-right: -15px;
  margin-left: -15px;
}
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-1,
  .col-md-2,
  .col-md-3,
  .col-md-4,
  .col-md-5,
  .col-md-6,
  .col-md-7,
  .col-md-8,
  .col-md-9,
  .col-md-10,
  .col-md-11,
  .col-md-12 {
    float: left;
  }
  .col-xs-1,
.col-sm-1,
.col-md-1,
.col-lg-1,
.col-xs-2,
.col-sm-2,
.col-md-2,
.col-lg-2,
.col-xs-3,
.col-sm-3,
.col-md-3,
.col-lg-3,
.col-xs-4,
.col-sm-4,
.col-md-4,
.col-lg-4,
.col-xs-5,
.col-sm-5,
.col-md-5,
.col-lg-5,
.col-xs-6,
.col-sm-6,
.col-md-6,
.col-lg-6,
.col-xs-7,
.col-sm-7,
.col-md-7,
.col-lg-7,
.col-xs-8,
.col-sm-8,
.col-md-8,
.col-lg-8,
.col-xs-9,
.col-sm-9,
.col-md-9,
.col-lg-9,
.col-xs-10,
.col-sm-10,
.col-md-10,
.col-lg-10,
.col-xs-11,
.col-sm-11,
.col-md-11,
.col-lg-11,
.col-xs-12,
.col-sm-12,
.col-md-12,
.col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-right: 15px;
  padding-left: 15px;
}
h2,
.h2 {
  font-size: 30px;
}
  h2,
  h3 {
    page-break-after: avoid;
  }
  .btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  -ms-touch-action: manipulation;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  padding: 6px 12px;
  font-size: 14px;
  line-height: 1.42857143;
  border-radius: 4px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
a {
  color: #337ab7;
  text-decoration: none;
}
  a,
  a:visited {
    text-decoration: underline;
  }
  a {
  background-color: transparent;
}
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>

    <div class="jumbotron">
        <h1>Enter Your Credentials</h1>
        <p class="lead">Name:&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:TextBox ID="TextBox1" runat="server" Width="415px"></asp:TextBox>
        </p>
        <p class="lead">Branch:&nbsp;&nbsp;
            <asp:TextBox ID="TextBox2" runat="server" Width="415px"></asp:TextBox>
        </p>
        <p class="lead">Rank:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:TextBox ID="TextBox3" runat="server" Width="417px"></asp:TextBox>
        </p>
        <h1>Enter Location</h1>
        <p class="lead">
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Use Curent Location" Width="211px" />
&nbsp;<asp:Label ID="Label1" runat="server"></asp:Label>
        </p>
        <p class="lead">Latitude:&nbsp;&nbsp;&nbsp;
            <asp:TextBox ID="TextBox4" runat="server"></asp:TextBox>
        </p>
        <p class="lead">Longitude:
            <asp:TextBox ID="TextBox5" runat="server"></asp:TextBox>
        </p>
    </div>

    <div class="row">
    </div>

        </div>
    </form>
</body>
</html>
