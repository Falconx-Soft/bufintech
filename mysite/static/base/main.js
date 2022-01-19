$(document).ready(function(){
    
    // $('#example_filter').hide();
    // $('#example_length').hide();
    // $('#example_info').hide();
    // $('#example_paginate').hide();

      // DataTable
	  
	if(!window.location.pathname.includes("analytical-applications") && !window.location.pathname.includes("aboutus") ){
		  var table = $('#example').DataTable({ "paging": false , 
			   "columnDefs": [
				{
					"targets":  JSON.parse(document.getElementById('hidden').textContent),
					"visible": false
				},
			],
    responsive: true
		  });
		  try{
			  var table1 = $('#example1').DataTable({ "paging": false,
				   "columnDefs": [
					{
						"targets":  JSON.parse(document.getElementById('hidden1').textContent),
						"visible": false
					}		  
			  ],
      responsive: true

		  });
		}
		catch(err){
			var table1;
		}
	  }

    // #market_search is a <input type="text"> element
    $('#market_search').on( 'change', function () {
        table
            .columns( 1 )
            .search( this.value )
            .draw();
    } );

    $('#investing_search_date').on( 'change', function () {
        table1
            .columns( 2 )
            .search( this.value )
            .draw();
    } );

    $('#trading_search_date').on( 'change', function () {
        table
            .columns( 2 )
            .search( this.value )
            .draw();
    } );

    // #epublic_search_ticker is a <input type="text"> element
    $('#epublic_search_ticker').on( 'change', function () {
      table
          .columns( 2 )
            .search( this.value )
            .draw();
    } );
    // #epublic_search is a <input type="text"> element
    $('#epublic_search_date').on( 'change', function () {
      table
          .columns( 3 )
            .search( this.value )
            .draw();
    } );

    // #learning_search is a <input type="text"> element
    $('#learning_search').on( 'change', function () {
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