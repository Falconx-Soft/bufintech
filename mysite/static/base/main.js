$(document).ready(function(){
	  
	if(!window.location.pathname.includes("analytical-apps") && !window.location.pathname.includes("aboutus") ){
		  var table = $('#example').DataTable({ "paging": false , 
			   "columnDefs": [
				{
					"targets":  JSON.parse(document.getElementById('hidden').textContent),
					"visible": true
				},
			],
    responsive: true
		  });
		  try{
			  var table1 = $('#example1').DataTable({ "paging": false,
				   "columnDefs": [
					{
						"targets":  JSON.parse(document.getElementById('hidden1').textContent),
						"visible": true
					}		  
			  ],
      responsive: true

		  });
		}
		catch(err){
			var table1;
		}
	}

  if(window.location.pathname.includes("market-outlook")){

    const market_search_country = document.getElementById("market_search_country");
    let temp = '<option value=>Search by Country</option>';
    table.column(1).data().unique().sort().each(function (d, j) {
      temp += '<option value="' + d + '">' + d + '</option>'
    });
    market_search_country.innerHTML = temp;

    const market_search_month = document.getElementById("market_search_month");
    let chkMonth = []
    let temp2 = '<option value=>Search by Month</option>';
    table.column(2).data().unique().sort().each(function (d, j) {
      let hold = d.split(" ");
      hold2 = hold[0]
      hold2 = hold2.replace(".", "")
      monthName = hold2
      if(!chkMonth.includes(monthName)){
        temp2 += '<option value="' + monthName + '">' + monthName + '</option>'
        chkMonth.push(monthName);
      }
    });
    market_search_month.innerHTML = temp2;

    const market_search_year = document.getElementById("market_search_year");
    let chkYear = []
    let temp3 = '<option value=>Search by Year</option>';
    table.column(2).data().unique().sort().each(function (d, j) {
      let y_hold = d.split(" ");
      y_hold2 = y_hold[2]
      YearName = y_hold2
      if(!chkYear.includes(YearName)){
        temp3 += '<option value="' + YearName + '">' + YearName + '</option>'
        chkYear.push(YearName);
      }
    });
    market_search_year.innerHTML = temp3;

    const market_search = document.getElementById("market_search");
    let chkDate = []
    let temp4 = '<option value=>Search by Date</option>';
    table.column(2).data().unique().sort().each(function (d, j) {
      let d_hold = d.split(" ");
      d_hold2 = d_hold[1]
      d_hold2 = d_hold2.replace(",", "")
      DateNumber = d_hold2
      if(!chkDate.includes(DateNumber)){
        temp4 += '<option value="' + DateNumber + '">' + DateNumber + '</option>'
        chkDate.push(DateNumber);
      }
    });
    chkDate.sort()
    for(let i=0; i<chkDate.length; i++){
      
    }
    market_search.innerHTML = temp4;

  }else if(window.location.pathname.includes("equity-research")){

    const epublic_search_year = document.getElementById("epublic_search_year");
    let chkYear = []
    let temp = '<option value=>Search by Year</option>';
    table.column(2).data().unique().sort().each(function (d, j) {
      let y_hold = d.split(" ");
      y_hold2 = y_hold[2]
      YearName = y_hold2
      if(!chkYear.includes(YearName)){
        temp += '<option value="' + YearName + '">' + YearName + '</option>'
        chkYear.push(YearName);
      }
    });
    epublic_search_year.innerHTML = temp;   
    
    const epublic_search_month = document.getElementById("epublic_search_month");
    let chkMonth = []
    let temp2 = '<option value=>Search by Month</option>';
    table.column(2).data().unique().sort().each(function (d, j) {
      let hold = d.split(" ");
      hold2 = hold[0]
      hold2 = hold2.replace(".", "")
      monthName = hold2
      if(!chkMonth.includes(monthName)){
        temp2 += '<option value="' + monthName + '">' + monthName + '</option>'
        chkMonth.push(monthName);
      }
    });
    epublic_search_month.innerHTML = temp2;

    const epublic_search_date = document.getElementById("epublic_search_date");
    let chkDate = []
    let temp4 = '<option value=>Search by Date</option>';
    table.column(2).data().unique().sort().each(function (d, j) {
      let d_hold = d.split(" ");
      d_hold2 = d_hold[1]
      d_hold2 = d_hold2.replace(",", "")
      DateNumber = d_hold2
      if(!chkDate.includes(DateNumber)){
        temp4 += '<option value="' + DateNumber + '">' + DateNumber + '</option>'
        chkDate.push(DateNumber);
      }
    });
    chkDate.sort()
    epublic_search_date.innerHTML = temp4;
    

  }else if(window.location.pathname.includes("learning-center")){
    const learning_search_year = document.getElementById("learning_search_year");
    let chkYear = []
    let temp = '<option value=>Search by Year</option>';
    table.column(3).data().unique().sort().each(function (d, j) {
      let y_hold = d.split(" ");
      y_hold2 = y_hold[2]
      YearName = y_hold2
      if(!chkYear.includes(YearName)){
        temp += '<option value="' + YearName + '">' + YearName + '</option>'
        chkYear.push(YearName);
      }
    });
    learning_search_year.innerHTML = temp; 

    const learning_search_month = document.getElementById("learning_search_month");
    let chkMonth = []
    let temp2 = '<option value=>Search by Month</option>';
    table.column(3).data().unique().sort().each(function (d, j) {
      let hold = d.split(" ");
      hold2 = hold[0]
      hold2 = hold2.replace(".", "")
      monthName = hold2
      if(!chkMonth.includes(monthName)){
        temp2 += '<option value="' + monthName + '">' + monthName + '</option>'
        chkMonth.push(monthName);
      }
    });
    learning_search_month.innerHTML = temp2;

    const learning_search_date = document.getElementById("learning_search_date");
    let chkDate = []
    let temp4 = '<option value=>Search by Date</option>';
    table.column(3).data().unique().sort().each(function (d, j) {
      let d_hold = d.split(" ");
      d_hold2 = d_hold[1]
      d_hold2 = d_hold2.replace(",", "")
      DateNumber = d_hold2
      if(!chkDate.includes(DateNumber)){
        temp4 += '<option value="' + DateNumber + '">' + DateNumber + '</option>'
        chkDate.push(DateNumber);
      }
    });
    chkDate.sort()
    learning_search_date.innerHTML = temp4;

  }else if(window.location.pathname.includes("money-making")){

    // *********************************** trading
    const trading_search_identifier = document.getElementById("trading_search_identifier");
    let temp = '<option value=>Search by Identifier</option>';
    table.column(3).data().unique().sort().each(function (d, j) {
      temp += '<option value="' + d + '">' + d + '</option>'
    });
    trading_search_identifier.innerHTML = temp;


    const trading_search_month = document.getElementById("trading_search_month");
    let chkMonth = []
    let m_temp2 = '<option value=>Search by Month</option>';
    table.column(2).data().unique().sort().each(function (d, j) {
      let m_hold = d.split(" ");
      m_hold2 = m_hold[0]
      m_hold2 = m_hold2.replace(".", "")
      monthName = m_hold2
      if(!chkMonth.includes(monthName)){
        m_temp2 += '<option value="' + monthName + '">' + monthName + '</option>'
        chkMonth.push(monthName);
      }
    });
    trading_search_month.innerHTML = m_temp2;

    const trading_search_year = document.getElementById("trading_search_year");
    let chkYear = []
    let y_temp = '<option value=>Search by Year</option>';
    table.column(2).data().unique().sort().each(function (d, j) {
      let y_hold = d.split(" ");
      y_hold2 = y_hold[2]
      YearName = y_hold2
      if(!chkYear.includes(YearName)){
        y_temp += '<option value="' + YearName + '">' + YearName + '</option>'
        chkYear.push(YearName);
      }
    });
    trading_search_year.innerHTML = y_temp;
    
    const trading_search_date = document.getElementById("trading_search_date");
    let chkDate = []
    let d_temp4 = '<option value=>Search by Date</option>';
    table.column(2).data().unique().sort().each(function (d, j) {
      let d_hold = d.split(" ");
      d_hold2 = d_hold[1]
      d_hold2 = d_hold2.replace(",", "")
      DateNumber = d_hold2
      if(!chkDate.includes(DateNumber)){
        d_temp4 += '<option value="' + DateNumber + '">' + DateNumber + '</option>'
        chkDate.push(DateNumber);
      }
    });
    chkDate.sort()
    trading_search_date.innerHTML = d_temp4;



    // *********************************** investing

    const investing_search_date = document.getElementById("investing_search_date");
    let chkDate_inv = []
    let d_temp4_inv = '<option value=>Search by Date</option>';
    table1.column(2).data().unique().sort().each(function (d, j) {
      let d_hold_inv = d.split(" ");
      d_hold2_inv = d_hold_inv[1]
      d_hold2_inv = d_hold2_inv.replace(",", "")
      DateNumber_inv = d_hold2_inv
      if(!chkDate_inv.includes(DateNumber_inv)){
        d_temp4_inv += '<option value="' + DateNumber_inv + '">' + DateNumber_inv + '</option>'
        chkDate_inv.push(DateNumber_inv);
      }
    });
    chkDate_inv.sort()
    investing_search_date.innerHTML = d_temp4_inv;

    const investing_search_month = document.getElementById("investing_search_month");
    let chkMonth_inv = []
    let m_temp2_inv = '<option value=>Search by Month</option>';
    table1.column(2).data().unique().sort().each(function (d, j) {
      let m_hold_inv = d.split(" ");
      m_hold2_inv = m_hold_inv[0]
      m_hold2_inv = m_hold2_inv.replace(".", "")
      monthName_inv = m_hold2_inv
      if(!chkMonth_inv.includes(monthName_inv)){
        m_temp2_inv += '<option value="' + monthName_inv + '">' + monthName_inv + '</option>'
        chkMonth_inv.push(monthName_inv);
      }
    });
    investing_search_month.innerHTML = m_temp2_inv;

    const investing_search_year = document.getElementById("investing_search_year");
    let chkYear_inv = []
    let y_temp_inv = '<option value=>Search by Year</option>';
    table1.column(2).data().unique().sort().each(function (d, j) {
      let y_hold_inv = d.split(" ");
      y_hold2_inv = y_hold_inv[2]
      YearName_inv = y_hold2_inv
      if(!chkYear_inv.includes(YearName_inv)){
        y_temp_inv += '<option value="' + YearName_inv + '">' + YearName_inv + '</option>'
        chkYear_inv.push(YearName_inv);
      }
    });
    investing_search_year.innerHTML = y_temp_inv;

    const investing_search_market = document.getElementById("investing_search_market");
    let temp2 = '<option value=>Search by Market</option>';
    table1.column(1).data().unique().sort().each(function (d, j) {
      temp2 += '<option value="' + d + '">' + d + '</option>'
    });
    investing_search_market.innerHTML = temp2;

    
    const investing_search_ticker = document.getElementById("investing_search_ticker");
    let temp3 = '<option value=>Search by Ticker</option>';
    table1.column(3).data().unique().sort().each(function (d, j) {
      temp3 += '<option value="' + d + '">' + d + '</option>'
    });
    investing_search_ticker.innerHTML = temp3;
  }else if(window.location.pathname.includes("news-letter")){

    const newsletter_search_year = document.getElementById("newsletter_search_year");
    let chkYear = []
    let temp = '<option value=>Search by Year</option>';
    table.column(0).data().unique().sort().each(function (d, j) {
      let y_hold = d.split(" ");
      y_hold2 = y_hold[2]
      YearName = y_hold2
      if(!chkYear.includes(YearName)){
        temp += '<option value="' + YearName + '">' + YearName + '</option>'
        chkYear.push(YearName);
      }
    });
    newsletter_search_year.innerHTML = temp; 


    const newsletter_search_month = document.getElementById("newsletter_search_month");
    let chkMonth = []
    let temp2 = '<option value=>Search by Month</option>';
    table.column(0).data().unique().sort().each(function (d, j) {
      let hold = d.split(" ");
      hold2 = hold[0]
      hold2 = hold2.replace(".", "")
      monthName = hold2
      if(!chkMonth.includes(monthName)){
        temp2 += '<option value="' + monthName + '">' + monthName + '</option>'
        chkMonth.push(monthName);
      }
    });
    newsletter_search_month.innerHTML = temp2;
    
    const newsletter_search_date = document.getElementById("newsletter_search_date");
    let chkDate = []
    let temp4 = '<option value=>Search by Date</option>';
    table.column(0).data().unique().sort().each(function (d, j) {
      let d_hold = d.split(" ");
      d_hold2 = d_hold[1]
      d_hold2 = d_hold2.replace(",", "")
      DateNumber = d_hold2
      if(!chkDate.includes(DateNumber)){
        temp4 += '<option value="' + DateNumber + '">' + DateNumber + '</option>'
        chkDate.push(DateNumber);
      }
    });
    chkDate.sort()
    newsletter_search_date.innerHTML = temp4;

  }

    function getMonth(m){
      if(m == "01"){
        return "Jan."
      }else if (m == "02"){
        return "Feb."
      }else if (m == "03"){
        return "Mar."
      }else if (m == "04"){
        return "Apr."
      }else if (m == "05"){
        return "May."
      }else if (m == "06"){
        return "Jun."
      }else if (m == "07"){
        return "July."
      }else if (m == "08"){
        return "Aug."
      }else if (m == "09"){
        return "Sept."
      }else if (m == "10"){
        return "Oct."
      }else if (m == "11"){
        return "Nov."
      }else if (m == "12"){
        return "Dec."
      }
    }

    function getDate(s_date){
      console.log(s_date);
      var n_date = s_date.split("/");
      var mon = getMonth(n_date[0]);
      var day = "";
      if(n_date[1][0] !== "0"){
        day = n_date[1]+",";
      }else{
        day = n_date[1][1]+",";
      }
      var year = n_date[2];

      console.log(mon+" "+day+" "+year);
      return mon+" "+day+" "+year
    }

    $('#newsletter_search_year').on('change', function(){
      table
        .columns( 0 )
        .search( this.value )
        .draw();
    });

    $('#newsletter_search_month').on('change', function(){
      table
        .columns( 0 )
        .search( this.value )
        .draw();
    });

    $('#newsletter_search_date').on('change', function(){
      table
        .columns( 0 )
        .search( this.value )
        .draw();
    });

    // #market_search is a <input type="text"> element
    $('#market_search').on( 'change', function () {
        table
            .columns( 2 )
            .search( this.value )
            .draw();
    } );
    
    $('#market_search_month').on( 'change', function () {
        table
            .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#market_search_year').on( 'change', function () {
        table
            .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#market_search_country').on( 'change', function () {
      table
          .columns( 1 )
          .search( this.value )
          .draw();
    } );

    $('#investing_search_date').on( 'change', function () {
      // if(this.value != ""){
      //     d = getDate(this.value)
      //   }else{
      //     d=""
      //   }
        table1
            .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#investing_search_month').on( 'change', function () {
        table1
            .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#investing_search_year').on( 'change', function () {
        table1
            .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#investing_search_market').on( 'change', function () {
        table1
            .columns( 1 )
            .search( this.value )
            .draw();
    } );

    $('#investing_search_ticker').on( 'change', function () {
      table1
          .columns( 3 )
          .search( this.value )
          .draw();
  } );

    $('#trading_search_date').on( 'change', function () {
      // if(this.value != ""){
      //     d = getDate(this.value)
      //   }else{
      //     d=""
      //   }
        table
            .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#trading_search_month').on( 'change', function () {
        table
            .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#trading_search_identifier').on( 'change', function () {
        table
            .columns( 3 )
            .search( this.value )
            .draw();
    } );

    // #epublic_search_ticker is a <input type="text"> element
    $('#epublic_search_ticker').on( 'change', function () {
      table
          .columns( 3 )
            .search( this.value )
            .draw();
    } );
    // #epublic_search is a <input type="text"> element
    $('#epublic_search_date').on( 'change', function () {
      table
          .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#epublic_search_month').on( 'change', function () {
        table
            .columns( 2 )
              .search( this.value )
              .draw();
      } );

      $('#trading_search_year').on( 'change', function () {
        table
            .columns( 2 )
              .search( this.value )
              .draw();
      } );

    $('#epublic_search_year').on( 'change', function () {
      table
          .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#epublic_search_market').on( 'change', function () {
      table
          .columns( 1 )
            .search( this.value )
            .draw();
    } );

    // #learning_search is a <input type="text"> element
    $('#learning_search').on( 'change', function () {
      table
          .columns( 1 )
            .search( this.value )
            .draw();
    } );

    $('#learning_search_class').on( 'change', function () {
      table
          .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#learning_search_date').on( 'change', function () {
      // if(this.value != ""){
      //     d = getDate(this.value)
      //   }else{
      //     d=""
      //   }
      table
          .columns( 3 )
            .search( this.value )
            .draw();
    } );

    $('#learning_search_month').on( 'change', function () {
      table
          .columns( 3 )
            .search( this.value )
            .draw();
    } );

    $('#learning_search_year').on( 'change', function () {
      table
          .columns( 3 )
            .search( this.value )
            .draw();
    } );

    // #company_search is a <input type="text"> element
    $('#company_search').on( 'change', function () {
      table
          .columns( 3 )
            .search( this.value )
            .draw();
    } );
	$('#equity_type').on('change',function(){	  
		  table
          .columns( 19 )
            .search( this.value )
            .draw();	  
	})
	
    $('#company_search1').on( 'change', function () {
		console.log(this.value);
      table1
          .columns( 3 )
            .search( this.value )
            .draw();
    } );	
    $('.datepicker').datepicker({
		    format: 'mm/dd/yyyy'
	});

    $('.nav-tabs a[href="#public"]').tab('show');
	$('.nav-tabs a[href="#systematic_trading"]').tab('show');

 });