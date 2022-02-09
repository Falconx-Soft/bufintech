$(document).ready(function(){
    
    // $('#example_filter').hide();
    // $('#example_length').hide();
    // $('#example_info').hide();
    // $('#example_paginate').hide();

      // DataTable
	  
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

    // #market_search is a <input type="text"> element
    $('#market_search').on( 'change', function () {
        if(this.value != ""){
          d = getDate(this.value)
        }else{
          d=""
        }
        table
            .columns( 2 )
            .search( d )
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
      if(this.value != ""){
          d = getDate(this.value)
        }else{
          d=""
        }
        table1
            .columns( 2 )
            .search( d )
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
      if(this.value != ""){
          d = getDate(this.value)
        }else{
          d=""
        }
        table
            .columns( 2 )
            .search( d )
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
      if(this.value != ""){
          d = getDate(this.value)
        }else{
          d=""
        }
      table
          .columns( 2 )
            .search( d )
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
      if(this.value != ""){
          d = getDate(this.value)
        }else{
          d=""
        }
      table
          .columns( 3 )
            .search( d )
            .draw();
    } );

    $('#learning_search_month').on( 'change', function () {
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