# odoo_datepicker
datepicker Plug-ins for odoo10
Example：<br/>
                &lt;field name='date' minDate='0'/> The minimum date is today<br/>
                &lt;field name='date' minDate='-1'/> The minimum date is the previous day (-2 is the day before, and so on)<br/>
                &lt;field name='date' minDate='1'/> The minimum date is the day after (2 is the last two days, and so on)<br/>
                &lt;field name='date' minDate='start_date'/> The minimum date to start_date prevail, if start_date no value, there is no limit<br/>
                &lt;field name='date' maxDate='0'/> The maximum date is today<br/>
                &lt;field name='date' maxDate='-1'/> The maximum date is the previous day (-2 is the day before, and so on)<br/>
                &lt;field name='date' maxDate='1'/> The maximum date is the day after (2 is the last two days, and so on)<br/>
                &lt;field name='date' maxDate='start_date'/> The maximum date to start_date prevail, if start_date no value, there is no limit<br/>
                <br/>
                If there are two fields from the start date, we can set it this way:<br/>
                &lt;field name='date_start' maxDate='date_end'/><br/>
                &lt;field name='date_end' minDate='date_start'/><br/>
