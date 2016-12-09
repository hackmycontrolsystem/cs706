var editor; // use a global for the submit and return data rendering in the examples
 
$(document).ready(function() {
    editor = new $.fn.dataTable.Editor( {
        //ajax: "../php/staff.php",
        table: "#example",
        fields: [ {
                label: "Type of atom",
                name: "type"
            }, {
                label: "Concentration of atom",
                name: "concentration"
            }, {
                label: "Mass of atom",
                name: "mass"
            }, {
                label: "Chemical potential of atom",
                name: "chemicalPotential"
            }
        ]
    } );
 
    var table = $('#example').DataTable( {
        lengthChange: false,
       // ajax: "../php/staff.php",
        columns: [
            { data: null, render: function ( data, type, row ) {
                // Combine the first and last names into a single table field
                return data.first_name+' '+data.last_name;
            } },
            { data: "type" },
            { data: "concentration" },
            { data: "mass" },
            { data: "chemicalPotential" }
            //,
            //{ data: "salary", render: $.fn.dataTable.render.number( ',', '.', 0, '$' ) }
        ],
        select: true
    } );
 
    // Display the buttons
    new $.fn.dataTable.Buttons( table, [
        { extend: "create", editor: editor },
        { extend: "edit",   editor: editor },
        { extend: "remove", editor: editor }
    ] );
 
    table.buttons().container()
        .appendTo( $('.col-sm-6:eq(0)', table.table().container() ) );
} );





function addRow() {
          
    var type = document.getElementById("type");
    var concentration = document.getElementById("concentration");
    var mass = document.getElementById("mass");
    var chemicalPotential = document.getElementById("chemicalPotential");
    var table = document.getElementById("myTableData");
 
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
 
    row.insertCell(0).innerHTML= '<input type="button" value = "Delete" onClick="Javacsript:deleteRow(this)">';
    row.insertCell(1).innerHTML= type.value;
    row.insertCell(2).innerHTML= concentration.value;
    row.insertCell(3).innerHTML= mass.value;
    row.insertCell(4).innerHTML= chemicalPotential.value;
 
}
 
function deleteRow(obj) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("myTableData");
    table.deleteRow(index);
    
}
 
function addTable() {
      
    var myTableDiv = document.getElementById("myDynamicTable");
      
    var table = document.createElement('TABLE');
    table.border='1';
    
    var tableBody = document.createElement('TBODY');
    table.appendChild(tableBody);
      
    for (var i=0; i<3; i++){
       var tr = document.createElement('TR');
       tableBody.appendChild(tr);
       
       for (var j=0; j<6; j++){
           var td = document.createElement('TD');
           td.width='75';
           td.appendChild(document.createTextNode("Cell " + i + "," + j));
           tr.appendChild(td);
       }
    }
    myTableDiv.appendChild(table);
    
}
 
function load() {
    console.log("Page load finished");
}

function validateForm() {
	//atomList
    var x = document.forms["mainForm"]["atomList_values"].value;
	for(var i=0; i<x.length; i++){
		if(document.forms["mainForm"]["type_atom"+i].value == null || document.forms["mainForm"]["type_atom"+i].value == ""){
			$(('#' + 'type_atom' + i)).addClass("requiredClass");
			$("#upload-file-info").html("Type of atom cannot be empty");
			return false;
		}else if(document.forms["mainForm"]["concentration_atom"+i].value == null || document.forms["mainForm"]["concentration_atom"+i].value == ""){
			$(('#' + 'concentration_atom' + i)).addClass("requiredClass");
			$("#upload-file-info").html("No. of atoms cannot be empty");
			return false;
		}else if(document.forms["mainForm"]["mass_atom"+i].value == null || document.forms["mainForm"]["mass_atom"+i].value == ""){
			$(('#' + 'mass_atom' + i)).addClass("requiredClass");
			$("#upload-file-info").html("Mass of atom cannot be empty");
			return false;
		}else if(document.forms["mainForm"]["potential_atom"+i].value == null || document.forms["mainForm"]["potential_atom"+i].value == ""){
			$(('#' + 'potential_atom' + i)).addClass("requiredClass");
			$("#upload-file-info").html("Chemical potential of atom cannot be empty");
			return false;
		}
	}
	return true;
}


document.getElementById('requiredClass').onchange = function (e) {
    var $this = $(this);
    var cID = $this.attr("id");
    var xVal = document.getElementById(cID).value;
    if(xVal == undefined || xVal == ''){
        $(('#' + cID)).addClass("requiredClass");
    }
    else if(xVal != undefined || xVal != ''){
        $(('#' + cID)).removeClass("requiredClass");
    }
}