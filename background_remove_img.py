package com.example.form
import com.example.form.DBHandler
import androidx.appcompat.app.AppCompatActivity
import android.os.PersistableBundle
import android.widget.Button
import android.widget.DatePicker
import android.widget.RadioGroup

import android.widget.EditText
import android.widget.Spinner
import android.widget.ArrayAdapter
import android.widget.RadioButton
import android.os.Bundle
import android.widget.Toast


class MainActivity : AppCompatActivity(){

    override fun onCreate(savedInstanceState: Bundle?, persistentState: PersistableBundle?) {
        val spinnerValues = listOf("BSIT", "BSCS", "BSSE")
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val submit: Button = findViewById(R.id.submit1)
        val degreeSpinner: Spinner = findViewById(R.id.degree)
        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_item, spinnerValues)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        degreeSpinner.adapter = adapter

        submit.setOnClickListener()
        {
            clicksubmitbutton()
        }



    }



    private fun clicksubmitbutton()
    {
        val rollnumber:EditText=findViewById(R.id.roll_number)
        val rolllnumber:String=rollnumber.text.toString()
        val name:EditText=findViewById(R.id.name)
        val name1:String=name.text.toString()
        val cgpa:EditText=findViewById(R.id.cgpa)
        val cgpa1:Double=cgpa.text.toString().toDouble()
        val spin:Spinner=findViewById(R.id.degree)
        val spindegree:String=spin.selectedItem.toString()
        val date:DatePicker=findViewById(R.id.datePicker)
        val datebirth:String=date.toString()
        val radioGroup: RadioGroup = findViewById(R.id.radiogroup)
        val selectedRadioButtonId: Int = radioGroup.checkedRadioButtonId
        val radiobutton:RadioButton=findViewById(selectedRadioButtonId)
        var radiobuttoncontent:String=radiobutton.text.toString()
        Toast.makeText(this,rolllnumber,Toast.LENGTH_SHORT).show()
    }

}



