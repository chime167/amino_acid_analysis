function runScan( term ) {
    // hide and clear the previous results, if any
    $('#result').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#analysis').serialize();
    
    $.ajax({
        url: './jones_final.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform protein analysis! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

function processJSON( data ) {
  var next_row_num = 1;
  $.each(data, function(i, item) {
    var this_row_id = 'result_row_' + next_row_num++;

    $('<tr/>', { "id" : this_row_id } ).appendTo('tbody');
    $('<td/>', { "text" : item.ID } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.Length } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.Weight } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.pI } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.Hydrophobicity } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.Instability_index } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.A } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.C } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.D } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.E } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.F } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.G } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.H } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.I } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.K } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.L } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.M } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.N } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.P } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.Q } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.R } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.S } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.T } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.V } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.W } ).appendTo('#' + this_row_id);
    $('<td/>', { "text" : item.Y } ).appendTo('#' + this_row_id);
  });
  $('#result').show()
}


$(document).ready(function () {

    $('#seqcheck').hide();
    let seqError = true;
    $('#sequence').keyup(function() {
      validateSeq();
    });

    function validateSeq() {
      var seqValue = $('#sequence').val().split('\n');
      if (seqValue.length == '') {
        $('#seqcheck').show();
          seqError = false;
          return false;
      }
      for (const s of seqValue) {
        if ((s.match(/^>[\s\S]+$/)) ||
        (s.match(/^[ARNDBCEQZGHILKMFPSTWXYV]+$/)) || (s.match(/^$/))) {
          $('#seqcheck').hide();
          seqError = true
        } 
        else {
          $('#seqcheck').show();
          $('#seqcheck').html
          ("** Please enter data in FASTA format!");
          seqError = false;
          return false;
        }
      }
      
    }
/*    $('#submit').click( function() {
      validateSeq();
      if (seqError === true) {
        return true;
      }
      else {
        return false;
      }
      
  });*/
  $('#submit').click( function() {
     if (seqError === true) {
      runScan();
     }
      return false;
    
  })

});
