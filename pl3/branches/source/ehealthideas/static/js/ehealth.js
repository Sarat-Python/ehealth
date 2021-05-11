	var baa=1;
	var textPadding = 3; // Padding at the left of tab text - bigger value gives you wider tabs
	var strictDocType = true;
	var tabView_maxNumberOfTabs = 6;	// Maximum number of tabs

	/* Don't change anything below here */
	var dhtmlgoodies_tabObj = new Array();
	var activeTabIndex = new Array();
	var MSIE = navigator.userAgent.indexOf('MSIE')>=0?true:false;

	var regExp = new RegExp(".*MSIE ([0-9]\.[0-9]).*","g");
	var navigatorVersion = navigator.userAgent.replace(regExp,'$1');

	var ajaxObjects = new Array();
	var tabView_countTabs = new Array();
	var tabViewHeight = new Array();
	var tabDivCounter = 0;
	var closeImageHeight = 8;	// Pixel height of close buttons
	var closeImageWidth = 8;	// Pixel height of close buttons


	function setPadding(obj,padding){
		var span = obj.getElementsByTagName('SPAN')[0];
		span.style.paddingLeft = padding + 'px';
		span.style.paddingRight = padding + 'px';
	}
	function showTab(parentId,tabIndex)
	{
		var parentId_div = parentId + "_";
		if(!document.getElementById('tabView' + parentId_div + tabIndex)){
			return;
		}
		if(activeTabIndex[parentId]>=0){
			if(activeTabIndex[parentId]==tabIndex){
				return;
			}

			var obj = document.getElementById('tabTab'+parentId_div + activeTabIndex[parentId]);

			obj.className='tabInactive';
			var img = obj.getElementsByTagName('IMG')[0];
			if(img.src.indexOf('tab_')==-1)img = obj.getElementsByTagName('IMG')[1];
			img.src = '/static/images/tab_right_inactive.gif';
			document.getElementById('tabView' + parentId_div + activeTabIndex[parentId]).style.display='none';
		}

		var thisObj = document.getElementById('tabTab'+ parentId_div +tabIndex);

		thisObj.className='tabActive';
		var img = thisObj.getElementsByTagName('IMG')[0];
		if(img.src.indexOf('tab_')==-1)img = thisObj.getElementsByTagName('IMG')[1];
		img.src = '/static/images/tab_right_active.gif';

		document.getElementById('tabView' + parentId_div + tabIndex).style.display='block';
		activeTabIndex[parentId] = tabIndex;


		var parentObj = thisObj.parentNode;
		var aTab = parentObj.getElementsByTagName('DIV')[0];
		countObjects = 0;
		var startPos = 2;
		var previousObjectActive = false;
		while(aTab){
			if(aTab.tagName=='DIV'){
				if(previousObjectActive){
					previousObjectActive = false;
					startPos-=2;
				}
				if(aTab==thisObj){
					startPos-=2;
					previousObjectActive=true;
					setPadding(aTab,textPadding+1);
				}else{
					setPadding(aTab,textPadding);
				}

				aTab.style.left = startPos + 'px';
				countObjects++;
				startPos+=2;
			}
			aTab = aTab.nextSibling;
		}

		return;
	}

	function tabClick()
	{
		var idArray = this.id.split('_');
		showTab(this.parentNode.parentNode.id,idArray[idArray.length-1].replace(/[^0-9]/gi,''));

	}

	function rolloverTab()
	{
		if(this.className.indexOf('tabInactive')>=0){
			this.className='inactiveTabOver';
			var img = this.getElementsByTagName('IMG')[0];
			if(img.src.indexOf('tab_')<=0)img = this.getElementsByTagName('IMG')[1];
			img.src = '/static/images/tab_right_over.gif';
		}

	}
	function rolloutTab()
	{
		if(this.className ==  'inactiveTabOver'){
			this.className='tabInactive';
			var img = this.getElementsByTagName('IMG')[0];
			if(img.src.indexOf('tab_')<=0)img = this.getElementsByTagName('IMG')[1];
			img.src = '/static/images/tab_right_inactive.gif';
		}

	}


	function initTabs(mainContainerID,tabTitles,activeTab,width,height,closeButtonArray,additionalTab)
	{
		if(!closeButtonArray)closeButtonArray = new Array();

		if(!additionalTab || additionalTab=='undefined'){
			dhtmlgoodies_tabObj[mainContainerID] = document.getElementById(mainContainerID);
			width = width + '';
			if(width.indexOf('%')<0)width= width + 'px';
			dhtmlgoodies_tabObj[mainContainerID].style.width = width;

			height = height + '';
			if(height.length>0){
				if(height.indexOf('%')<0)height= height + 'px';
				dhtmlgoodies_tabObj[mainContainerID].style.height = height;
			}


			tabViewHeight[mainContainerID] = height;

			var tabDiv = document.createElement('DIV');
			var firstDiv = dhtmlgoodies_tabObj[mainContainerID].getElementsByTagName('DIV')[0];

			dhtmlgoodies_tabObj[mainContainerID].insertBefore(tabDiv,firstDiv);
			tabDiv.className = 'dhtmlgoodies_tabPane';
			tabView_countTabs[mainContainerID] = 0;

		}else{
			var tabDiv = dhtmlgoodies_tabObj[mainContainerID].getElementsByTagName('DIV')[0];
			var firstDiv = dhtmlgoodies_tabObj[mainContainerID].getElementsByTagName('DIV')[1];
			height = tabViewHeight[mainContainerID];
			activeTab = tabView_countTabs[mainContainerID];


		}



		for(var no=0;no<tabTitles.length;no++){
			var aTab = document.createElement('DIV');
			aTab.id = 'tabTab' + mainContainerID + "_" +  (no + tabView_countTabs[mainContainerID]);
			aTab.onmouseover = rolloverTab;
			aTab.onmouseout = rolloutTab;
			aTab.onclick = tabClick;
			aTab.className='tabInactive';
			tabDiv.appendChild(aTab);
			var span = document.createElement('SPAN');
			span.innerHTML = tabTitles[no];
			span.style.position = 'relative';
			aTab.appendChild(span);

			

			var img = document.createElement('IMG');
			img.valign = 'bottom';
			img.src = '/static/images/tab_right_inactive.gif';
			// IE5.X FIX
			if((navigatorVersion && navigatorVersion<6) || (MSIE && !strictDocType)){
				img.style.styleFloat = 'none';
				img.style.position = 'relative';
				img.style.top = '4px'
				span.style.paddingTop = '4px';
				aTab.style.cursor = 'hand';
			}	// End IE5.x FIX
			aTab.appendChild(img);
		}

		var tabs = dhtmlgoodies_tabObj[mainContainerID].getElementsByTagName('DIV');
		var divCounter = 0;
		for(var no=0;no<tabs.length;no++){
			if(tabs[no].className=='dhtmlgoodies_aTab' && tabs[no].parentNode.id == mainContainerID){
				if(height.length>0)tabs[no].style.height = height;
				tabs[no].style.display='none';
				tabs[no].id = 'tabView' + mainContainerID + "_" + divCounter;
				divCounter++;
			}
		}
		tabView_countTabs[mainContainerID] = tabView_countTabs[mainContainerID] + tabTitles.length;
		showTab(mainContainerID,activeTab);

		return activeTab;
	}

	function showAjaxTabContent(ajaxIndex,parentId,tabId)
	{
		var obj = document.getElementById('tabView'+parentId + '_' + tabId);
		obj.innerHTML = ajaxObjects[ajaxIndex].response;
	}


	function getTabIndexByTitle(tabTitle)
	{
		var regExp = new RegExp("(.*?)&nbsp.*$","gi");
		tabTitle = tabTitle.replace(regExp,'$1');
		for(var prop in dhtmlgoodies_tabObj){
			var divs = dhtmlgoodies_tabObj[prop].getElementsByTagName('DIV');
			for(var no=0;no<divs.length;no++){
				if(divs[no].id.indexOf('tabTab')>=0){
					var span = divs[no].getElementsByTagName('SPAN')[0];
					var regExp2 = new RegExp("(.*?)&nbsp.*$","gi");
					var spanTitle = span.innerHTML.replace(regExp2,'$1');

					if(spanTitle == tabTitle){

						var tmpId = divs[no].id.split('_');
						return Array(prop,tmpId[tmpId.length-1].replace(/[^0-9]/g,'')/1);
					}
				}
			}
		}

		return -1;

	}

	/* Call this function if you want to display some content from external file in one of the tabs
	Arguments: Title of tab and relative path to external file */

	function addAjaxContentToTab(tabTitle,tabContentUrl)
	{
		var index = getTabIndexByTitle(tabTitle);
		if(index!=-1){
			var ajaxIndex = ajaxObjects.length;

			tabId = index[1];
			parentId = index[0];


			ajaxObjects[ajaxIndex] = new sack();
			ajaxObjects[ajaxIndex].requestFile = tabContentUrl;	// Specifying which file to get

			ajaxObjects[ajaxIndex].onCompletion = function(){ showAjaxTabContent(ajaxIndex,parentId,tabId); };	// Specify function that will be executed after file has been found
			ajaxObjects[ajaxIndex].runAJAX();		// Execute AJAX function

		}
	}
/* div hiding for signup*/
	
	function getSelect(s) 
	{
	  var selected;
	selected= s.options[s.selectedIndex].value;
	//document.write(selected);
	if(selected=="user")
	{
		document.getElementById("user").style.visibility = 'visible';
		document.getElementById("doc").style.visibility = 'hidden';
		document.getElementById("hosp").style.visibility = 'hidden';
		document.getElementById("bbank").style.visibility = 'hidden';
		document.getElementById("pharmacy").style.visibility = 'hidden';
	}
	else if(selected=="doctor")
		{
		document.getElementById("doc").style.visibility = 'visible';
		document.getElementById("user").style.visibility = 'hidden';
		document.getElementById("hosp").style.visibility = 'hidden';
		document.getElementById("bbank").style.visibility = 'hidden';
		document.getElementById("pharmacy").style.visibility = 'hidden';
		}
	else if(selected=="hospital")
	{
		document.getElementById("hosp").style.visibility = 'visible';
		document.getElementById("user").style.visibility = 'hidden';
		document.getElementById("doc").style.visibility = 'hidden';
		document.getElementById("bbank").style.visibility = 'hidden';
		document.getElementById("pharmacy").style.visibility = 'hidden';
	}
	else if(selected=="blood bank")
	{
		document.getElementById("hosp").style.visibility = 'hidden';
		document.getElementById("user").style.visibility = 'hidden';
		document.getElementById("doc").style.visibility = 'hidden';
		document.getElementById("bbank").style.visibility = 'visible';
		document.getElementById("pharmacy").style.visibility = 'hidden';
	}
	else if(selected=="pharmacy")
	{
		document.getElementById("hosp").style.visibility = 'hidden';
		document.getElementById("user").style.visibility = 'hidden';
		document.getElementById("doc").style.visibility = 'hidden';
		document.getElementById("bbank").style.visibility = 'hidden';
		document.getElementById("pharmacy").style.visibility = 'visible';
	}
	
	}
function defualt() 
{
	document.getElementById("user").style.visibility = 'visible';
	document.getElementById("doc").style.visibility = 'hidden';
	document.getElementById("hosp").style.visibility = 'hidden';
	document.getElementById("bbank").style.visibility = 'hidden';
	document.getElementById("pharmacy").style.visibility = 'hidden';
}
function defaultdoctor() 
{
	document.getElementById("user").style.visibility = 'hidden';
	document.getElementById("doc").style.visibility = 'visible';
	document.getElementById("hosp").style.visibility = 'hidden';
	document.getElementById("bbank").style.visibility = 'hidden';
	document.getElementById("pharmacy").style.visibility = 'hidden';
}


Element.extend(
{
	hide: function() 
	{
		return this.setStyle('display', 'none');
	},
	
	show: function() 
	{
		return this.setStyle('display', '');
	}
});

var DropdownMenu = new Class({	
	initialize: function(element)
	{
		$A($(element).childNodes).each(function(el)
		{
			if(el.nodeName.toLowerCase() == 'li')
			{
				$A($(el).childNodes).each(function(el2)
				{
					if(el2.nodeName.toLowerCase() == 'ul')
					{
						$(el2).hide();
						
						el.addEvent('mouseover', function()
						{
							el2.show();
							return false;
						});

						el.addEvent('mouseout', function()
						{
							el2.hide();
						});
						new DropdownMenu(el2);
					}
				});
			}
		});
		return this;
	}
});

Window.onDomReady(function() {new DropdownMenu($('dropdownMenu'))});







function CalcIt(form) {
var Age = Number(form.Years.value);

var weight =  Number(form.wt.value);

if (!checkWeight(weight)) return false;
if (form.wu.selectedIndex == 0) { // 0 = weight in lbs
	kg = weight * 0.45359237;
} else {  // 1 = weight in kg.
	kg = weight;
}
if (kg < 10) {
	alert("Weights should be heavier than 10 kilograms (22 pounds).");
	return false;
}
if (kg > 200) {
	alert("Weights should be lighter than 200 kilograms (441 pounds).");
	return false;
}


var height =  Number(form.ht.value);

if ((isNaN(height)) || (height == null)  || (height == "") || (height < 0)) {
	feetAndInches(form);
	height =  Number(form.ht.value);
}

if (form.hu.selectedIndex == 0) {		//  if height units are "inches"
	heightInches = height;
	heightMeters = height * 2.54 / 100;
} else {					// else if height units are "cm".
	heightInches = height / 2.54;
	heightMeters = height / 100;
}
if (heightMeters < 0.33) {
	alert("Heights should be taller than 33 centimeters (31.5 inches).");
	return false;
}
if (heightMeters > 2.41) {
	alert("Heights should be shorter than 241 centimeters ( 7 feet, 11 inches).");
	return false;
}
setFeetAndInches(form,heightInches);

var cm = heightMeters * 100;

if ((isNaN(Age)) || (Age == null)  || (Age == "")) Age = GetAge(form,cm);

if ( Age < 1 ) {
	return false;
} else {
	if (Age > 120) {
		Age = 75;
		form.Years.value = 75;
	}
}
SetAgeCat(form,Age);

if (form.Gender.selectedIndex == 0) { // 0 = boys.
	if (Age < 12 && cm > 170) {  // If Age is small, is Height too big? 
		Age = 25;
		form.Years.value = Age;
	}
			
	//  or is Height too small, if Age is adult?	
	if ( cm < 155 && Age > 17 ) {  // Use 155 ( 5'1") as min male Adult height.
		Age = rounding( (0.0003*cm*cm) + (0.0847*cm) - 7.5544,1);  // median Age for Height.
		form.Years.value = Age;
	}

} else {  // 1 is girls
	if (Age < 12 && cm > 170  ) {  // If Age is small, is Height too big? 
		Age = 25;
		form.Years.value = Age;
	}	
	
	//  or is Height too small, if Age is adult?
	if ( cm < 145 && Age > 17 ) {  // Use 145 ( 4'9") as min female Adult height.
		Age = rounding( (0.0007*cm*cm) - (0.0136*cm) - 1.6819,0);  // median Age for Height.
		form.Years.value = Age;
	}
}

// Calculate BMI
bmi = kg / Math.pow(heightMeters,2);
form.bmi.value = rounding(bmi,1);

// Set Body Description based on bmi percentiles.
var b85 = 25;  
var b05 = 17;  
var b95 = 30;  
var b75 = 25;
var a2 = Age*Age;
var a3 = a2*Age;
var a4 = a2*a2;

var hadj = 0;  // Height adjustment for women.
// This algorithm is copyright. Don't steal it.
if (form.Gender.selectedIndex == 1) {	// sex is female.
if ( Age < 14 ) {  // was 16.
 b85 = 0.000283*a4 - 0.01751*a3 + 0.3673*a2 - 2.3464*Age + 21.352;
 b05 = -0.00016*a4 + 0.00429*a3 + 0.0043*a2 - 0.4246*Age + 15.107;
 b95 = 0.000485*a4 - 0.0268*a3 + 0.5096*a2 - 2.926*Age + 23.164;
} else {
 b05 = 20 * ( 1 - Math.exp(-1*(0.11*Age)));
 b95 = (31.1*Age)/(2.0+Age);
 if ( Age < 25 ) {
    if ( form.cdc.selectedIndex == 0 ) { // If using CDC.
	    b85 = 0.000283*a4 - 0.01751*a3 + 0.3673*a2 - 2.3464*Age + 21.352;
	  } else {   // Or, if using halls.md v2
          b85 = 0.002855*a3 - 0.1909*a2 + 4.2262*Age - 6.1898;  // Curvy part.
	  }
 } else {
    b85 = (28.5*(Age+8))/(5 +(Age+8));
 }
}
if ( Age < 12) {
b75 = b85;
} else {
b75 = 24.5 *(1-Math.exp(-0.1*(Age+10)));
}
if ( Age > 22 ) {  // Allow short women to have higher BMIs than tall women.
	hadj = -1.6 + ( 3.2 /(1 + Math.pow(1.18,cm-163.5) ));
	// window.defaultStatus = "hadj = " + rounding( hadj ,5);
	hadj = hadj * (0.125*Math.min(Age,30) - 2.75);   // Age 22=0 up to Age 30=1, 1 thereafter.
	b85 = b85 + hadj;
	b95 = b95 + hadj;
	b05 = b05 + hadj;	
	b75 = b75 + hadj;
}
// Read Copyright warning at http://www.halls.md/steve/copyright.htm
} else {  // Male
if ( Age < 17 ) {  // was 16.
 b85 =  0.000223*a4 - 0.0139*a3 + 0.3082*a2 - 2.105*Age + 21.254;
 b05 = -0.000143*a4 + 0.0037*a3 + 0.015*a2  - 0.5188*Age + 15.677;
 b95 =  0.000536*a4 - 0.0288*a3 + 0.5394*a2 - 3.2219*Age + 23.811;
} else {
 b05 = 20.7 * ( 1 - Math.exp(-1*(0.115*(Age-0.9))));
 b85 = (29.1*(Age-8))/(1.5+(Age-8));
 b95 = (33.3*Age)/(2.9+Age);
}
if (Age < 15)	{
b75 = b85;
} else {
b75 = 25.5 *(1-Math.exp(-0.1*(Age+10)));
}
}

if (form.cdc.selectedIndex == 0 ) {  // If CDC classification, truncate
	b95 = Math.min( b95, 30 );   // at their Maximum boundaries.
b85 = Math.min( b85, 25 );
//if ( Age > 18 ) {
//	b95 = 30;
//	b85 = 25;	
//}
b75 = b85;   // ... and don't use "Marginally Overweight" category.
}
if (Age < 15 ) {
b75 = b85;  //  .. and don't use "Marginally Overweight" below Age 15.
}

var interp = "Obese";
if ( bmi < b95 ) interp = "Overweight";
if ( bmi < b85 ) interp = "Marginally Overweight";
if ( bmi < b75 ) interp = "In Normal Range";
if ( bmi < b05 ) interp = "Underweight";
if (bmi < 13 || bmi > 50) interp = "Check your numbers";

form.interp.value = interp;


// Prepare vars for percentile calculations.
var p05 = 0;
var p10 = 0;
var p25 = 0;
var p50 = 0;
var p75 = 0;
var p90 = 0;
var p95 = 0;

var m = 0;
var b = 0;
var theP = 0;
var specific50 = 0; // Use for age-specific like 50th percentile value.
var diff50 = 0;	 // holds the difference of p50 - specific50.

a2 = cm*cm;
a3 = a2*cm;

// Calculate Weight for Height percentiles based on age.
if (form.Gender.selectedIndex == 0) { // 0 = boys.
	if (cm<125) {  // 2nd order polynomials
		p05 = 0.0021*a2 - 0.155*cm + 8.2203;
		p10 = 0.0023*a2 - 0.1823*cm + 9.618;
		p25 = 0.0028*a2 - 0.2744*cm + 14.483;
		p50 = 0.0026*a2 - 0.21*cm + 10.8;
		p75 = 0.0037*a2 - 0.3934*cm + 19;
		p90 = 0.0058*a2 - 0.7611*cm + 35.6;
		p95 = 0.0082*a2 - 1.2204*cm + 58.051;
	} else {
		if (cm < 165) {   // sigmoid curves
			p05 = 20+(70-20)/(1+(Math.pow(10,(158-cm)*0.04)));
			p10 = 23+(67-23)/(1+(Math.pow(10,(156-cm)*0.05)));
			p25 = 24+(75-24)/(1+(Math.pow(10,(156-cm)*0.05)));
			p50 = 22.9+(89-22.9)/(1+(Math.pow(10,(156-cm)*0.045)));
			p75 = 27.5+(90-27.5)/(1+(Math.pow(10,(153-cm)*0.055)));
			p90 = 30+(94-30)/(1+(Math.pow(10,(150-cm)*0.055)));
			p95 = 34.5+(104-34.5)/(1+(Math.pow(10,(151-cm)*0.056)));
		} else {   // linear
			p05 = 0.73*cm - 67.96;
			p10 = 0.7928*cm - 75.507;
			p25 = 0.8941*cm - 86.397;
			p50 = 0.9165*cm - 81.496;
			p75 = 1.1124*cm - 105.3;
			p90 = 1.2251*cm - 114.72;
			p95 = 1.2363*cm - 108.84;
		}
	}
	specific50 = p50;
	if ( Age > 18 ) {  // Adjustment for adults. Age checking >17 ensures,
			   // that cm > 155 for males, and cm > 145 for females.
		specific50 = (0.85*cm) - (0.0086*Age*Age - 0.9796*Age +92.781);
	} else {  
		if ( Age > 7 ) {  // Ages 7 thru 18.   ( Ages < 12 will have cm < 170. )
			specific50 = (17+(80-17)/(1+Math.pow(10,(154-cm)*0.03))) + Math.max((1.018*Age - 15),0)*Math.min((0.0278*cm - 3.4722),1);
			//  specific = baseline + ((age adjust 13-18) gives 0 to 1) * (cm of 125 to 161 gives 0 to 1)
		}
	}
	if (cm < 112)  {  // 125 works better for girls.
		specific50 = p50;
	}
} else {	// 1 = girls.
	// Get p05 thru p95 ready, we'll need them later.
	if (cm<125) {   // 2nd order polynomials
		p05 = 0.0020*a2 - 0.141*cm + 8.0736;
		p10 = 0.0022*a2 - 0.177*cm + 10;
		p25 = 0.0016*a2 - 0.0398*cm + 2.9072;
		p50 = 0.0018*a2 - 0.0554*cm + 3.3595;
		p75 = 0.0033*a2 - 0.3099*cm + 14.6;
		p90 = 0.0045*a2 - 0.46*cm + 19.2;
		p95 = 0.0061*a2 - 0.7332*cm + 31.202;
	} else {
		if (cm < 161) {  // sigmoid curves
			p05 = 21+(53-21)/(1+(Math.pow(10,(148-cm)*0.06)));
			p10 = 21.7+(53-21.7)/(1+(Math.pow(10,(146-cm)*0.07)));
			p25 = 22+(60-22)/(1+(Math.pow(10,(145-cm)*0.068)));
			p50 = 22+(70-22)/(1+(Math.pow(10,(143-cm)*0.065)));
			p75 = 25+(82-25)/(1+(Math.pow(10,(143-cm)*0.068)));
			p90 = 26+(99-26)/(1+(Math.pow(10,(142-cm)*0.06)));
			p95 = 28+(107-28)/(1+(Math.pow(10,(142-cm)*0.06)));
		} else {   // linear
			p05 = 0.6153*cm - 50.992;
			p10 = 0.6759*cm - 58.085;
			p25 = 0.6375*cm - 45.456;
			p50 = 0.6261*cm - 33.83;
			p75 = 0.6896*cm - 30.833;
			p90 = 0.8127*cm - 36.131;
			p95 = cm - 58;
			
		}
	}
	specific50 = p50;
	if ( Age > 18 ) {  // Adjustment for adults. Age checking >17 ensures,
						// that cm > 155 for males, and cm > 145 for females.
		specific50 = (0.6261*cm) - ( 0.0094*Age*Age - 1.1097*Age + 59.183);
	} else {  
		if ( Age > 7 ) {  // Ages 7 thru 18.   ( Ages < 12 will have cm < 170. )
			specific50 = (13+(75-13)/(1+Math.pow(10,(150-cm)*0.026))) + Math.max((1.018*Age - 13.234),0)*Math.min((0.0278*cm - 3.4722),1);
			//  specific = baseline + ((age adjust 13-18) gives 0 to 1) * (cm of 125 to 161 gives 0 to 1)
		}
	}
	if (cm < 126)  {  // 111 works better for boys.
		specific50 = p50;
	}
}

diff50 = p50 - specific50;
p05 = p05 - diff50;
p10 = p10 - diff50;
p25 = p25 - diff50;
p50 = p50 - diff50;
p75 = p75 - diff50;
p90 = p90 - diff50;
p95 = p95 - diff50;

if (kg < p10) {
	m = (10-5) / (p10-p05);
	b = 5 - (m * p05);
} else {
	if (kg < p25) {
		m = (25-10) / (p25-p10);
		b = 10 - (m * p10);
	} else {
		if (kg < p50) {
			m = (50-25) / (p50-p25);
			b = 25 - (m * p25);
		} else {
			if (kg < p75) {
				m = (75-50) / (p75-p50);
				b = 50 - (m * p50);
			} else {
				if (kg < p90) {
					m = (90-75) / (p90-p75);
					b = 75 - (m * p75);
				} else {	// 90th percentile or higher.
					m = (95-90) / (p95-p90);
					b = 90 - (m * p90);
				}
			}
		}
	}	
}
theP = m * kg + b;	// Don't forget to truncate >98% or < 2% values.

form.kgcmP.value = SetPercentile( rounding( theP,0) );



return null;
}

//This is only called if the form.Years.value was empty.
//The user may have used the pop-up menu however, to set an age.
function GetAge(form,cm) {
var tempAge = 35;
if (form.AgeCat.selectedIndex == 0) { // 70+ years,
	tempAge = 75;
} else {
	if (form.AgeCat.selectedIndex < 6) { // 1 thru 5 are decades 20s thru 60s.
		tempAge = 65 - (form.AgeCat.selectedIndex -1)*10;
	} else {
		if (form.AgeCat.selectedIndex == 6 ) {
			tempAge = 19;
		} else {
			if (form.AgeCat.selectedIndex < 23) { // 7 thru 22 are ages 17 thru 2.
				tempAge = 17 - (form.AgeCat.selectedIndex-7);
			} else {
				if (form.AgeCat.selectedIndex == 23) { // age 1.5 yrs.
					tempAge = 1.5;
				} else {
					if (form.AgeCat.selectedIndex == 24) {	// age 1 yrs.
						tempAge = 1;
					} else {
						if (form.AgeCat.selectedIndex == 25) {
							tempAge = 35;
						} else {	// selectedIndex == 26  for Child.
							tempAge = 17.5;  // Force a tempAge adjustment
						}			// based on height, below.
					}
				}
			}
		}
	}
}
if (form.Gender.selectedIndex == 0) { // 0 = boys.
	if ( cm < 155 && tempAge > 17 ) {  // Use 155 ( 5'1") as min male Adult height.
		tempAge = rounding(0.0003*cm*cm + 0.0847*cm - 7.5544,1);  // median Age for Height.
	}
} else {  // 1 is girls
	if ( cm < 145 && tempAge > 17 ) {  // Use 145 ( 4'9") as min female Adult height.
		tempAge = rounding(0.0007*cm*cm - 0.0136*cm - 1.6819,1);  // median Age for Height.
	}
}
form.Years.value = tempAge;
return tempAge;
}

function SetAge(form) {
if (form.Years.value > 0) {	// Only change the Age field, if a value is already there.

	if (form.AgeCat.selectedIndex == 0) { // 70+ years,
		form.Years.value = 75;
	} else {
		if (form.AgeCat.selectedIndex < 6) { // 1 thru 5 are decades 20s thru 60s.
			form.Years.value = 65 - (form.AgeCat.selectedIndex -1)*10;
		} else {
			if (form.AgeCat.selectedIndex == 6 ) {
				form.Years.value = 19;
			} else {
				if (form.AgeCat.selectedIndex < 23) { // 7 thru 22 are ages 17 thru 2.
					form.Years.value = 17 - (form.AgeCat.selectedIndex-7);
				} else {
					if (form.AgeCat.selectedIndex == 23) { // age 1.5 yrs.
						form.Years.value = 1.5;
					} else {
						if (form.AgeCat.selectedIndex == 24) {	// age 1 yrs.
							form.Years.value = 1;
						} else {
							if (form.AgeCat.selectedIndex == 25) {
								form.Years.value = 30;
							} else {
								if (form.Years.value > 19) form.Years.value = "";
							}
						}
					}
				}
			}
		}
	}
}
return true;
}

function SetAgeCat(form,tAge) {	
if (tAge > 69.99) { form.AgeCat.selectedIndex = 0; } // 70+ years,
else { if (tAge <=1) form.AgeCat.selectedIndex = 24; 	// age 1 yrs.
else { if (tAge < 2) form.AgeCat.selectedIndex = 23; // age 1.5 yrs.
else { if (tAge < 18) form.AgeCat.selectedIndex = -Math.floor(tAge) + 24;  // 7 thru 22 are ages 17 thru 2.
else { if (tAge < 20) form.AgeCat.selectedIndex = 6;   // age 18-19
else { // 1 thru 5 are decades 60s thru 20s. 1=60s 2=50s 3=40s
	form.AgeCat.selectedIndex = Math.ceil(-1*(tAge-78.999))/10; 
}}}}}
return true;
}

function setFeetAndInches(form,inchies) {
var feet = Math.min( Math.max( Math.floor( inchies / 12 ), 1), 7);
form.htf.selectedIndex = feet - 1;

inchies = rounding( inchies - feet*12,0);
form.hti.selectedIndex = Math.min( Math.max( inchies,0), 11 );
return true;
}

function feetAndInches(form) {
var inchies = 0;
inchies = ((form.htf.selectedIndex+1) * 12) + form.hti.selectedIndex;

if (form.hu.selectedIndex == 0) form.ht.value = inchies;
if (form.hu.selectedIndex == 1) form.ht.value = rounding( inchies * 2.54,0);
return true;
}


function SetPercentile( pc ) {

if (pc > 98) { pc = "> 98th percentile"; }
else { if (pc < 2) { pc = "< 2nd percentile"; }
else { if (pc == 11) { pc = "11th percentile"; }
else { if (pc == 12) { pc = "12th percentile"; }
else { if (pc == 13) { pc = "13th percentile"; }
else { if (rightDigit(pc) == 1) { pc = pc + "st percentile"; }
else { if (rightDigit(pc) == 2) { pc = pc + "nd percentile"; }
else { if (rightDigit(pc) == 3) { pc = pc + "rd percentile"; } 
else { pc = pc + "th percentile"; }
}}}}}}}

return pc;
}

function poundsAndKilos(form) {
var weight = Number(form.wt.value);
if ( weight > 0) {
	if (form.wu.selectedIndex == 0) {	// 0 = pounds.
		form.wt.value = rounding( weight / 0.45359237,0);
	} else {								// 1 = kilograms.
		if (weight > 219) {
			form.wt.value = rounding( weight * 0.45359237,0);
		} else {
			form.wt.value = rounding( weight * 0.45359237,1);
		}
	}
	form.wt.select();
	form.wt.focus();
}
return true;
}

function inchesCm(form) {
var height = Number(form.ht.value);
if (height > 0) {
	if (form.hu.selectedIndex == 0) { // is now inches, was cm.
		setFeetAndInches(form, height / 2.54); 
		form.ht.value = rounding( height / 2.54,1) ; 
	} else {								// is now cm, was inches.
		setFeetAndInches(form, height);  // Always pass inches in height to this function.
		form.ht.value = rounding( height * 2.54,0);  }  
	form.ht.select();
	form.ht.focus();
}
return true;
}

function rightDigit(num) {
num = num - (Math.floor(num/10)*10);
return num;
}

function rounding(number,decimal) {
multi = Math.pow(10,decimal);
number = Math.round(number * multi) / multi;
return number;
}


function checkWeight(val) {
if ((isNaN(val)) || (val == null)  || (val == "") || (val < 0)) {
	alert( "Please enter a value for Weight.");
	return false;
}
return true;
}

function OpenLink(theURL) {
window.open(theURL);
return true;
}


function microsoftKeyPress() {
if (window.event.keyCode == 13) {
CalcIt(document.forms[0]);
}
return true;
}

setTimeout("document.forms[0].wt.focus();",1);

//-->

function showtextbox(s)
{
	 var selected;
		selected= s.options[s.selectedIndex].value;
		//document.write(selected);
	  if(selected=="others"){
		  if( baa==1){
		  	var tbl = document.getElementById('foobar');
		    var row = tbl.insertRow(3);
		//    var textNode = document.createTextNode("         ");
		    var cellLeft = row.insertCell(0);
		    var textNode = document.createTextNode("*Specialization:");
		     //textNode.style.text-align='right';
		     cellLeft.appendChild(textNode);
		    
		    // right cell
		    var cellRight = row.insertCell(1);
		    var el1 = document.createElement('input');
		    
		    el1.value = '';
		    el1.style.width = '300px';
		    el1.type = 'text';
		    el1.id = 'specialization2';
		    el1.name = 'specialization2';
		   /* alert(el.name);*/
		    cellRight.appendChild(el1);
baa=baa+1;
		  }
	}
	}