# -*- coding: utf-8 -*-

import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

opts = Options()  # options for chromedriver
opts.add_argument("--window-size=1000,1000")  # specifies window width,height
# opts.add_argument("headless")  # runs without the browser visible
exe_path = chromedriver_binary.chromedriver_filename
chromedriver = None # initialize chromedriver global variable.

# TODO: fix warning
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
def start_chromedriver():
	global chromedriver  # use the global chromedriver variable.
	chromedriver = webdriver.Chrome(executable_path=exe_path, options=opts)
	chromedriver.get('https://www.myalcon-toriccalc.com/#/calculator')
	time.sleep(1)  # give page a chance to load

def quit_chromedriver():
	global chromedriver  # use the global chromedriver variable.
	chromedriver.quit()

def county_and_language_page():
	global chromedriver
	# https://www.myalcon-toriccalc.com/#/countryLanguage
	country_select_elem = Select(chromedriver.find_element(By.ID, 'countrydropDown'))
	if country_select_elem is not None:
		country_select_elem.select_by_value('0')  # "United States"
		language_select_elem = Select(chromedriver.find_element(By.ID, 'languagedropDown'))
		language_select_elem.select_by_value('0')  # "English")
		language_continue_elem = chromedriver.find_element(By.ID, 'countryLanguageContinue')
		language_continue_elem.click()
		time.sleep(1)

def terms_and_conditions():
	global chromedriver
	# https://www.myalcon-toriccalc.com/#/termsConditions
	terms_checkbox_elem = chromedriver.find_element(By.ID, 'termsConditionsIAgree')
	if terms_checkbox_elem is not None:
		terms_checkbox_elem.click()
		terms_continue_elem = chromedriver.find_element(By.ID, 'termsConditionsContinue')
		terms_continue_elem.click()
		time.sleep(1)

def input_dummy_names():
	global chromedriver
	surgeon_name_elem = chromedriver.find_element(By.NAME, 'surgeonNameTextbox')
	patient_name_elem = chromedriver.find_element(By.NAME, 'patientFirstNametextBox')
	surgeon_name_elem.send_keys("Demo Surgeon")
	patient_name_elem.send_keys("Demo Patient")

def run_form(patient_data):
	global chromedriver
	start_chromedriver()
	county_and_language_page()
	terms_and_conditions()
	input_dummy_names()  # needs to happen first before the rest of the form input
	

## SAMPLE VALUES FOR DEMONSTRATION
patient_data = { 'IOL_model':    'Alcon SN60WF', 
				 'mfr':          'Alcon',
				 'model':        'Alcon - SN60WF/SA60WF',
				 'eye_side':     'R',
				 'axial_length':  25,
				 'meas_K1':       45, 
				 'meas_K2':       46, 
				 'optical_ACD':   3.56,
				 'gender':        'M',
				 'target_PO_rx':  0  # default value
				}  # DEBUG samples

# process main method call
if __name__ == '__main__':
	run_form(patient_data)



	# https://www.myalcon-toriccalc.com/
	# did it resolve to 
	# https://www.myalcon-toriccalc.com/#/calculator

# calculate_button_elem    = chromedriver.find_element(By.Name, 'buttonCalculate')  # <button type="submit">
# clear_fields_button_elem = chromedriver.find_element(By.Name, 'buttonReset')      # <button type="button">



# <select name="productdropdown" class="col-input select form-control ng-pristine 
# ng-valid ng-valid-required ng-touched" style="border-radius:10px;" 
# ng-model="selectedProduct" ng-options="product.productName group by product.grouping for product in products" 
# ng-change="productChange()" tabindex="3" 
# ng-disabled="(calculatorForm.patientFirstNametextBox.$invalid || calculatorForm.surgeonNameTextbox.$invalid)" 
# ng-required="true" required="required">
# <option value="" disabled="" selected="" data-i18n="ProductDefault" class="">Select Alcon Toric product</option>
# <optgroup label="AcrySof®">
# <option value="0" label="IQ Toric SN6ATx">IQ Toric SN6ATx</option>
# <option value="1" label="UV Only Toric SA6ATx">UV Only Toric SA6ATx</option>
# <option value="2" label="ReSTOR® Toric +3.0 SND1Tx">ReSTOR® Toric +3.0 SND1Tx</option>
# <option value="3" label="ReSTOR® Toric +2.5 SV25Tx">ReSTOR® Toric +2.5 SV25Tx</option>
# <option value="4" label="UV Only ReSTOR® Toric +2.5 SA25Tx">UV Only ReSTOR® Toric +2.5 SA25Tx</option>
# <option value="5" label="IQ PanOptix® Toric TFNTx0">IQ PanOptix® Toric TFNTx0</option>
# <option value="6" label="UV Only PanOptix® Toric TFATx0">UV Only PanOptix® Toric TFATx0</option>
# <option value="7" label="IQ Vivity™ Toric DFTx15">IQ Vivity™ Toric DFTx15</option>
# <option value="8" label="UV Only Vivity™ Toric DATx15">UV Only Vivity™ Toric DATx15</option></optgroup></select>

# # these are in order they appear in the dropdown, could be referenced using list index and value parameter (int) in option tag.
# models = ["IQ Toric SN6ATx", "UV Only Toric SA6ATx", "ReSTOR® Toric +3.0 SND1Tx",
# 		  "ReSTOR® Toric +2.5 SV25Tx", "UV Only ReSTOR® Toric +2.5 SA25Tx", "IQ PanOptix® Toric TFNTx0",
# 		  "UV Only PanOptix® Toric TFATx0", "IQ Vivity™ Toric DFTx15", "UV Only Vivity™ Toric DATx15"]

# # YOU HAVE TO RE-SELECT PRODUCT IF YOU SELECT an eye and then select another eye; the form remembers your selections.
# # no eye is default selected.
# # may have to click the label, I think the element may occlude the actual radio button.
# <label for="eyeSelectRightEye" data-i18n="EyeSelectRightEyeLabel" tabindex="4" ng-keypress="selectEyeKey($event, 'Right')">Right Eye</label>
# <input type="radio" class="radio-custom radio-big right ng-untouched ng-valid ng-pristine" id="eyeSelectRightEye" name="formEye" value="Right" ng-model="preopData.eyeType" ng-click="eyeChanged(preopData)" ng-disabled="(preopData.eyeType === 'Right' || calculatorForm.patientFirstNametextBox.$invalid || calculatorForm.surgeonNameTextbox.$invalid)">

# <label for="eyeSelectLeftEye" data-i18n="EyeSelectLeftEyeLabel" tabindex="5" ng-keypress="selectEyeKey($event, 'Left')">Left Eye</label>
# <input type="radio" class="radio-custom radio-big left ng-untouched ng-valid ng-valid-parse ng-pristine" id="eyeSelectLeftEye" name="formEye" value="Left" ng-model="preopData.eyeType" ng-click="eyeChanged(preopData)" ng-disabled="(preopData.eyeType === 'Left' || calculatorForm.patientFirstNametextBox.$invalid || calculatorForm.surgeonNameTextbox.$invalid)" disabled="disabled">



# # have to pick one of these radio buttons; again, 
# # may have to click the label, I think the element may occlude the actual radio button.
# <input type="radio" name="formulaRadio" id="formulaBarrett" class="radio-custom radio-grey radio-big ng-untouched ng-valid ng-valid-required ng-pristine" ng-value="formulas[0]" ng-model="preopData.formula" ng-click="formulaChanged(preopData)" required="" ng-hide="!selectedCountry.barrettEnabled" ng-disabled="(noEyeSelected) || selectedProduct.productId == null" value="[object Object]">
# <label tabindex="6" data-i18n="BarrettLabel" for="formulaBarrett" ng-keypress="selectFormulaKey($event, 'Barrett')">Barrett</label>

# <input type="radio" name="formulaRadio" id="formulaHolladayI" class="radio-custom radio-grey radio-big ng-untouched ng-valid ng-valid-required ng-pristine" ng-value="formulas[1]" ng-model="preopData.formula" ng-click="formulaChanged(preopData)" required="" ng-disabled="(noEyeSelected) || selectedProduct.productId == null" value="[object Object]">
# <label tabindex="7" data-i18n="HolladayILabel" for="formulaHolladayI" ng-keypress="selectFormulaKey($event, 'HolladayI')">Holladay</label>



# # if Holladay is picked, only Axial length (mm) is an input option; 
# # checkbox is default-checked (Total Sia for a small 2.5mm temporal corneal incision) and 
# # the following fields in the bottom-most box are grayed out: total SIA, flattening meridian, both empty,
# # and incision location is fixed at 180 degrees, and K index is set to 1.3375 (what barrett and Hoffer are default set to)
# # IF YOU UNCHECK IT: bottom fields shift to : surgically induced astigmatiasm (SIA),
# #  incision location (default 180 degrees) becomes settable, and K index is set to 1.3375 .

# # if Barrett is picked:
# # axial length is an option:
# <input name="axialLengthTextbox" type="text" class="form-control form-input-ctrl ng-pristine ng-invalid ng-invalid-required ng-invalid-digit-restriction ng-touched" ng-model="preopData.eyeData.axialLength" ng-model-options="{ allowInvalid: true }" ng-change="hideResults()" digit-restriction="" restrict-max="38" restrict-min="14" restrict-precision="2" restrict-len="5" required="" tabindex="8" ng-disabled="(noEyeSelected) || selectedProduct.productId == null">
# # anterior chamber depth is an option:
# <input name="anteriorChamberDepthTextbox" type="text" class="form-control form-input-ctrl ng-pristine ng-untouched ng-invalid ng-invalid-required ng-invalid-restrict-min ng-invalid-digit-restriction" ng-model="preopData.eyeData.anteriorChamberDepth" ng-model-options="{ allowInvalid: true }" ng-change="hideResults()" digit-restriction="" restrict-max="6" restrict-min="1" restrict-precision="2" restrict-len="5" required="" tabindex="9" ng-disabled="(noEyeSelected) || selectedProduct.productId == null">



