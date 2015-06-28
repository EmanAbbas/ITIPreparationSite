
$(document).ready(function(){/* jQuery toggle layout */
    $('#btnToggle').click(function(){
      if ($(this).hasClass('on')) {
        $('#main .col-md-6').addClass('col-md-4').removeClass('col-md-6');
        $(this).removeClass('on');
      }
      else {
        $('#main .col-md-4').addClass('col-md-6').removeClass('col-md-4');
        $(this).addClass('on');
      }
    });



});


function Vote(type, id, vote,event){


        $.post('/vote/', {id:id, type:type, vote:vote}, function(response) {
                if (response) {
                    $('#'+type+id).text(response.votes);
                }
            });
        event.preventDefault();
    }

function approveQuestion(id){


        $.post('/approve/question', {id:id}, function(response) {
                if (response.status == 'SUCCESS') {
                    $('#'+id).remove();

                }
            });

    }


function rejectQuestion(id){


        $.post('/reject/question', {id:id}, function(response) {
                if (response.status == 'SUCCESS') {
                    $('#'+id).remove();

                }
            });

    }





function approveAnswer(id){


        $.post('/approve/answer', {id:id}, function(response) {
                if (response.status == 'SUCCESS') {
                    $('#'+id).remove();

                }
            });

    }


function rejectAnswer(id){


        $.post('/reject/answer', {id:id}, function(response) {
                if (response.status == 'SUCCESS') {
                    $('#'+id).remove();

                }
            });

    }




function approveMaterial(id){


        $.post('/approve/material', {id:id}, function(response) {
                if (response.status == 'SUCCESS') {
                    $('#'+id).remove();

                }
            });

    }


function rejectMaterial(id){


        $.post('/reject/material', {id:id}, function(response) {
                if (response.status == 'SUCCESS') {
                    $('#'+id).remove();

                }
            });

    }


function notification_read(target_id){
    $.post('/notify/read', {target_id:target_id}, function(response) {
                if (response.status == 'SUCCESS') {
                    $('#'+target_id).remove();
                    $('#notify').val($('#notify').val() - 1 );

                }
            });
}