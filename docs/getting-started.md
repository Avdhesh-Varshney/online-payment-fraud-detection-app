# Building the application 

## Application Code 

=== "Details of the User"

    ??? info "User Details Code"
        ```py
        def userDetails():
            st.subheader('Provide your details')

            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Enter your name", key="name", placeholder="John Doe")
            with col2:
                age = st.number_input("Enter your age", min_value=1, key="age")
            
            col3, col4 = st.columns(2)
            with col3:
                phone_extension = st.text_input("Enter your phone extension", key="phone_extension", placeholder="+91")
            with col4:
                phone = st.text_input("Enter your phone number", key="phone", placeholder="1234567890")
            phone_no = f"{phone_extension} {phone}"

            st.markdown("#### Your Home Address")
            col5, col6 = st.columns(2)
            with col5:
                street = st.text_input("Street", key="street", placeholder="123, Example Street")
            with col6:
                city = st.text_input("City", key="city", placeholder="Example City")
            col7, col8, col9 = st.columns(3)
            with col7:
                state = st.text_input("State", key="state", placeholder="Example State")
            with col8:
                country = st.text_input("Country", key="country", placeholder="Example Country")
            with col9:
                postal_code = st.number_input("Postal Code", min_value=10000, max_value=999999, step=1, value=123456, key="postal_code")
            my_address_data = {"Street": street, "City": city, "State": state, "Country": country, "Postal Code": postal_code}
            my_address = f"{street}, {city}, {state}, {country}, {postal_code}"

            if st.checkbox("Correspondence Address same as Home Address", key="corr_address"):
                corr_address_data = my_address_data
                corr_address = my_address
            else:
                st.markdown("#### Your Correspondence Address")
                col10, col11 = st.columns(2)
                with col10:
                corr_street = st.text_input("Street", key="corr_street", placeholder="123, Example Street")
                with col11:
                corr_city = st.text_input("City", key="corr_city", placeholder="Example City")
                col12, col13, col14 = st.columns(3)
                with col12:
                corr_state = st.text_input("State", key="corr_state", placeholder="Example State")
                with col13:
                corr_country = st.text_input("Country", key="corr_country", placeholder="Example Country")
                with col14:
                corr_postal_code = st.number_input("Postal Code", min_value=10000, max_value=999999, step=1, value=123456, key="corr_postal_code")
                corr_address_data = {"Street": corr_street, "City": corr_city, "State": corr_state, "Country": corr_country, "Postal Code": corr_postal_code}
                corr_address = f"{corr_street}, {corr_city}, {corr_state}, {corr_country}, {corr_postal_code}"

            st.divider() ############################################################################################################
            return name, age, phone_no, my_address_data, my_address, corr_address_data, corr_address

        ```
    
    ```py
    name, age, phone_no, my_address_data, my_address, corr_address_data, corr_address = userDetails()
    ```

=== "Details of the Transaction"

    ??? info "Transaction Details Code"
        ```py
        def transactionDetails(labels, my_address_data, my_address):
            st.subheader('Provide the transaction details')

            # For TransactionDT 
            START_DATE = '2017-12-01'
            StartDate = datetime.datetime.strptime(START_DATE, "%Y-%m-%d")
            col1, col2 = st.columns(2)
            with col1:
                TransactionDT_date = st.date_input("Transaction Date", key="TransactionDT_date")
            with col2:
                TransactionDT_time = st.time_input("Transaction Time", step=60, key="TransactionDT_time")
            TransactionDateTime = datetime.datetime.combine(TransactionDT_date, TransactionDT_time)
            TransactionDT = int((TransactionDateTime - StartDate).total_seconds())
            
            # For TransactionID, TransactionAmt 
            cols = st.columns(2)
            with cols[0]:
                TransactionID = st.number_input("Transaction ID", key="TransactionID", min_value=1000000, max_value=999999999999, value=123456789012, placeholder="7-12 Digits")
            with cols[1]:
                TransactionAmt = np.log(st.number_input("Transaction Amount", min_value=0.1, value=1.0, step=1.0, key="TransactionAmt"))

            # For min_last, max_last, mean_last, std_last
            min_last, max_last = st.slider("Your usual transaction amount range", min_value=1, max_value=100000, value=(10500, 70000), step=10, key="min_max_last")
            mean_last = np.log(np.mean([min_last, max_last]))
            std_last = mean_last / np.log(np.std([min_last, max_last]))

            # For dist1
            dist1 = st.slider("Distance from the home location (in km)", min_value=0, max_value=10000, value=100, step=1, key="dist1")

            # For _Weekdays, _Hours, _Days 
            _Weekdays, _Hours, _Days = TransactionDateTime.weekday(), TransactionDateTime.hour, TransactionDateTime.day 

            # For ProductCD 
            ProductCD = labels[st.selectbox("What type of item is being purchased?", ["Widgets", "Clothing", "Retail", "Healthcare", "Subscription"], key="ProductCD").lower()[0]]

            # For P_emaildomain, R_emaildomain
            col3, col4 = st.columns(2)
            with col3:
                purchaser_email = st.text_input("Purchaser Email Address", key="puchaser_email", placeholder="user@example.example")
                P_emaildomain = purchaser_email.split('@')[-1] or 'nan'
                if P_emaildomain not in list(labels.keys()):
                P_emaildomain = 'nan'
                P_emaildomain = labels[P_emaildomain]
            with col4:
                recipient_email = st.text_input("Recipient Email Address", key="recipient_email", placeholder="user@example.example")
                R_emaildomain = recipient_email.split('@')[-1] or 'nan'
                if R_emaildomain not in list(labels.keys()):
                R_emaildomain = 'nan'
                R_emaildomain = labels[R_emaildomain]
            
            col5, col6 = st.columns(2)
            with col5:
                tx_phone_extension = st.text_input("Enter the phone extension", key="tx_phone_extension", placeholder="+91")
            with col6:
                tx_phone = st.text_input("Enter transaction phone number", key="tx_phone", placeholder="1234567890")
            tx_phone_no = f"{tx_phone_extension} {tx_phone}"

            if st.checkbox("Transaction Address same as Home Address", key="tx_address", value=True):
                tx_address_data = my_address_data
                tx_address = my_address
            else:
                st.markdown("##### From where did you conduct your transaction?")
                col7, col8 = st.columns(2)
                with col7:
                tx_street = st.text_input("Street", key="tx_street", placeholder="123, Example Street")
                with col8:
                tx_city = st.text_input("City", key="tx_city", placeholder="Example City")
                col9, col10, col11 = st.columns(3)
                with col9:
                tx_state = st.text_input("State", key="tx_state", placeholder="Example State")
                with col10:
                tx_country = st.text_input("Country", key="tx_country", placeholder="Example Country")
                with col11:
                tx_postal_code = st.number_input("Postal Code", min_value=10000, max_value=999999, step=1, value=123456, key="tx_postal_code")
                tx_address_data = {"Street": tx_street, "City": tx_city, "State": tx_state, "Country": tx_country, "Postal Code": tx_postal_code}
                tx_address = f"{tx_street}, {tx_city}, {tx_state}, {tx_country}, {tx_postal_code}"

            # For addr1, addr2, first_value_addr1 
            addr1 = float(str(tx_address_data['Postal Code'])[3:])
            addr2 = float(str(tx_address_data['Postal Code'])[:3])
            first_value_addr1 = float(str(tx_address_data['Postal Code'])[0])

            st.divider() ############################################################################################################
            return TransactionDT, TransactionID, TransactionAmt, mean_last, min_last, max_last, std_last, dist1, _Weekdays, _Days, _Hours, \
                ProductCD, purchaser_email, P_emaildomain, recipient_email, R_emaildomain, tx_phone_no, tx_address_data, tx_address, addr1, addr2, \
                first_value_addr1
        ```

    ```py
    (TransactionDT, TransactionID, TransactionAmt, 
    mean_last, min_last, max_last, std_last, dist1, 
    _Weekdays, _Days, _Hours, ProductCD, 
    purchaser_email, P_emaildomain, recipient_email, R_emaildomain, 
    tx_phone_no, tx_address_data, tx_address, 
    addr1, addr2, first_value_addr1) = transactionDetails(labels, my_address_data, my_address)
    ```

=== "Details of the Card"

    ??? info "Card Details Code"
        ```py
        def cardDetails(labels, TransactionAmt):
            st.subheader("Provide the card details")

            # For Card_ID
            cols = st.columns(5)
            with cols[0]:
                st.text_input("Card ID", key="Card_ID", label_visibility="hidden", value="Card ID", disabled=True)
            with cols[1]:
                card1 = st.text_input("Card ID 1", key="card1", label_visibility="hidden", value="1000", placeholder="1000")
                first_value_card1 = float(card1[0])
            with cols[2]:
                card2 = st.text_input("Card ID 2", key="card2", label_visibility="hidden", value="5552", placeholder="5552")
            with cols[3]:
                card3 = st.text_input("Card ID 3", key="card3", label_visibility="hidden", value="1835", placeholder="1835")
            with cols[4]:
                card5 = st.text_input("Card ID 5", key="card5", label_visibility="hidden", value="2246", placeholder="2246")
            Card_ID = f"{card1} {card2} {card3} {card5}"

            # Card Holder Name
            card_holder_name = st.text_input("Card Holder Name", key="card_holder_name", placeholder="John Doe")

            # For TransactionAmt_to_mean_card_id, TransactionAmt_to_mean_card1, TransactionAmt_to_mean_card4
            max_limit = st.number_input("Maximum transaction limit of this card", min_value=1, value=100000, step=10, key="max_limit")
            min_last, max_last = st.slider("Your usual transaction amount range through this card", min_value=1, max_value=100000 if max_limit == 1 else max_limit, value=(1, max_limit), step=1, key="min_max_last_card")
            std_last = np.log(np.mean([min_last, max_last])) / np.log(np.std([min_last, max_last]))
            TransactionAmt_to_mean_card_id = np.exp(TransactionAmt) - np.mean([min_last, max_last])
            TransactionAmt_to_mean_card1 = np.exp(TransactionAmt) / np.mean([min_last, max_last])
            TransactionAmt_to_mean_card4 = abs((np.exp(TransactionAmt) / np.mean([min_last, max_last])) - std_last)

            # For card1, card2, card4 
            payment_method = st.selectbox("Have you made the payment using a card?", ['Select One', 'Yes', 'No'], key="payment_method")
            card4, card6 = -999, -999
            if payment_method == 'Yes':
                card4 = labels[st.selectbox("Brand of the card", ['Visa', 'Mastercard', 'American Express', 'Discover'], key="card4").lower()]
                card6 = labels[st.selectbox("Usage of the card", ['Credit', 'Debit', 'Debit or Credit', 'Charge Card'], key="card6").lower()]
            card_data = {"Card1": card1, "Card2": card2, "Card3": card3, "Card4": card4, "Card5": card5, "Card6": card6}

            st.divider() ############################################################################################################
            return card_data, Card_ID, first_value_card1, card_holder_name, TransactionAmt_to_mean_card_id, TransactionAmt_to_mean_card1, TransactionAmt_to_mean_card4
        ```
    
    ```py
    (card_data, Card_ID, first_value_card1, card_holder_name, 
    TransactionAmt_to_mean_card_id, TransactionAmt_to_mean_card1,
    TransactionAmt_to_mean_card4) = cardDetails(labels, TransactionAmt)
    ```

=== "Billing Details"

    ??? info "Billing Details Code"
        ```py
        def billingDetails(purchaser_email, card_holder_name, name, phone_no, tx_phone_no, my_address, tx_address, country, tx_country):
            st.subheader("Provide the billing details")

            # For M1, M4, M5, M6, M7 
            # M1 -> Billing Address == Shipping Address
            M1 = st.selectbox("Is the billing address the same as the shipping address?", ['Select One', 'Yes', 'No'], key="M1")
            M1 = 1 if M1 == 'Yes' else 2 if M1 == 'No' else -999

            # M2 -> Email Address (at T/X) == Email Address (Owner)
            email_tx = st.text_input("Email Address at the Transaction Receipt", key="email_tx", placeholder="user@example.example")
            M2 = -999 if email_tx == '' or purchaser_email == '' else 1 if email_tx == purchaser_email else 2

            # M3 -> Card Holder Name == Name of the Owner
            M3 = -999 if card_holder_name == '' or name == '' else 1 if card_holder_name == name else 2

            # M4 -> T/X from same device as last transaction
            M4 = st.selectbox("Have you done the transaction from the same device as last time?", ['Select One', 'Yes', 'No'], key="M4_device")
            if M4 == 'Yes':
                M4 = st.selectbox("Have you done the transaction from a nearby home location?", ['Select One', 'Yes', 'No'], key="M4_home")
                M4 = 4 if M4 == 'Yes' else 5 if M4 == 'No' else -999
            elif M4 == 'No':
                M4 = 3
            else:
                M4 = -999

            # M5 -> Phone Number (at T/X) == Phone Number of the Owner
            M5 = -999 if phone_no == ' ' or len(phone_no) < 14 or tx_phone_no == ' ' or len(tx_phone_no) < 14 else 1 if phone_no == tx_phone_no else 2

            # M6 -> Address (at T/X) == Address of the Owner
            M6 = -999 if my_address == ", , , , 123456" or tx_address == ", , , , 123456" else 1 if my_address == tx_address else 2

            # M7 -> Country (at T/X) == Country of the Owner
            M7 = -999 if country == '' or tx_country == '' else 1 if country == tx_country else 2

            M_data = {"M1": M1, "M2": M2, "M3": M3, "M4": M4, "M5": M5, "M6": M6, "M7": M7}
            st.divider() ############################################################################################################
            return M_data
        ```

    ```py
    M_data = billingDetails(purchaser_email, card_holder_name, name, phone_no, 
                            tx_phone_no, my_address, tx_address,
                            my_address_data['Country'], tx_address_data['Country'])
    ```

=== "Customer Behaviourial Details"

    ??? info "Behaviourial Details Code"
        ```py
        def behavioralDetails(TransactionAmt, min_last, max_last, _Hours, my_address_data, tx_address_data):
            # For V1, V12, V14, V35, V41, V65, V69, V75, V88, V94, V241
            st.subheader("Provide the transactional usage details")

            cols = st.columns(3)
            with cols[0]:
                V1 = st.selectbox("Have you recently changed your account information?", ['Select One', 'Yes', 'No'], key="V1")
                V1 = 1 if V1 == 'No' else 0
            with cols[1]:
                V14 = st.selectbox("Have you encountered any other fraud scenarios?", ['Select One', 'Yes', 'No'], key="V14")
                V14 = 1 if V14 == 'No' else 0
            with cols[2]:
                V88 = st.selectbox("Is this transaction done from your own device?", ['Select One', 'Yes', 'No'], key="V88")
                V88 = 1 if V88 == 'Yes' else 0

            # Is the transaction amount significantly higher than the user's maximum?
            V41 = 1 if (np.exp(TransactionAmt) > max_last) else 0

            # Was this transaction made within normal business hours?
            V65 = 1 if (8 <= _Hours <= 18) else 0

            # Is the user's transaction history within the expected range for their account?
            V241 = 1 if (min_last <= np.exp(TransactionAmt) <= max_last) else 0

            V94 = st.selectbox("What is the nature of your purchase history?", ['Select One', 'Mostly small transactions', 'A mix of small and large transactions', 'Mostly large transactions'], key="V94")
            V94 = (0 if V94 == 'Mostly small transactions' else 1 if V94 == 'A mix of small and large transactions' else 2) / 2

            # 0 Exactly the same address, 1 Same city but different street, 2 Same state but different city, 3 Same country but different state
            V12 = abs(0 if my_address_data == tx_address_data else 1 if my_address_data['City'] == tx_address_data['City'] else 2 if my_address_data['State'] == tx_address_data['State'] else 3 if my_address_data['Country'] == tx_address_data['Country'] else -1) / 3

            V35 = st.selectbox("How long has your account been active?", ['Select One', 'Less than 1 month', '1-6 months', '6-12 months', 'More than a year'], key="V35")
            V35 = (0 if V35 == 'More than a year' else 1 if V35 == '6-12 months' else 2 if V35 == '1-6 months' else 3) / 3

            V75 = st.selectbox("How often do you change your password?", ['Select One', 'Less than once a year', 'Once a year', 'Every 6 months', 'Every 3 months', 'Monthly'], key="V75")
            V75 = (0 if V75 == 'Less than once a year' else 1 if V75 == 'Once a year' else 2 if V75 == 'Every 6 months' else 3 if V75 == 'Every 3 months' else 4) / 4

            V69 = st.selectbox("How frequently do you make transactions online?", ['Select One', 'Daily', 'Weekly', 'Bi-weekly', 'Monthly', 'Every few months', 'Rarely'], key="V69")
            V69 = (0 if V69 == 'Daily' else 1 if V69 == 'Weekly' else 2 if V69 == 'Bi-weekly' else 3 if V69 == 'Monthly' else 4 if V69 == 'Every few months' else 5) / 5

            V_data = {"V1": V1, "V12": V12, "V14": V14, "V35": V35, "V41": V41, "V65": V65, "V69": V69, "V75": V75, "V88": V88, "V94": V94, "V241": V241}

            # For C5, C6, C7, C9, C12, C14
            st.divider() ############################################################################################################
            time_tx = st.expander("Transaction Details", expanded=True)
            with time_tx:
                st.markdown("<div style='text-align: justify; margin: 1rem;'>\
                            <p style='margin-bottom: 5px;'>Ranges of the transaction amount:</p>\
                            <b>Small Transactions:</b> 1 - 1000<br />\
                            <b>Medium Transactions:</b> 1000 - 20000<br />\
                            <b>Large Transactions:</b> 20000 - 100000<br />\
                            <b>Very Large Transactions:</b> 100000 - more than 100000<br />\
                            </div>", unsafe_allow_html=True)

            st.subheader("Provide the transactional behavior details")
            C7 = st.slider("How frequently do small transactions occur per day?", min_value=0, max_value=100, value=5, step=1, key="C7") / 2256
            C12 = st.slider("How frequently do large transactions occur per day?", min_value=0, max_value=10, value=2, step=1, key="C12") / 3188

            C6 = st.slider("How frequently do small transactions occur per week?", min_value=0, max_value=1000, value=30, step=1, key="C6") / 2252
            C14 = st.slider("How frequently do large transactions occur per week?", min_value=0, max_value=100, value=13, step=1, key="C14") / 1429

            C5 = st.slider("How frequently do small transactions occur per month?", min_value=0, max_value=10000, value=200, step=1, key="C5") / 376
            C9 = st.slider("How frequently do large transactions occur per month?", min_value=0, max_value=1000, value=30, step=1, key="C9") / 572

            C_data = {"C5": C5, "C6": C6, "C7": C7, "C9": C9, "C12": C12, "C14": C14}

            # For D2, D3, D4, D5, D11
            st.divider() ############################################################################################################
            st.subheader("Provide the transaction time behavioral details")

            D2 = st.slider("How many days between small transactions?", min_value=0, max_value=100, value=2, step=1, key="D2") / 641
            D11 = st.slider("How many days between medium transactions?", min_value=0, max_value=365, value=15, step=1, key="D11") / 936
            D3 = st.slider("How many days between large transactions?", min_value=0, max_value=730, value=40, step=1, key="D3") / 1076
            D5 = st.slider("How many days between very large transactions?", min_value=0, max_value=730, value=80, step=1, key="D5") / 1088
            D4 = st.slider("How many days between exceptional transactions?", min_value=0, max_value=1095, value=200, step=1, key="D4") / 1213

            D_data = {"D2": D2, "D3": D3, "D4": D4, "D5": D5, "D11": D11}
            st.divider() ############################################################################################################
            return V_data, C_data, D_data
        ```
    
    ```py
    V_data, C_data, D_data = behavioralDetails(TransactionAmt, min_last, max_last, _Hours, my_address_data, tx_address_data)
    ```

=== "Device Information"

    ??? info "Device Info. Code"
        ```py
        def deviceInfo(labels):
            st.subheader("Provide the device details")

            # For DeviceType
            DeviceType = st.selectbox("Device Type", ['Select One', 'Desktop', 'Mobile'], key="DeviceType")
            DeviceType = 1 if DeviceType == 'Desktop' else 2 if DeviceType == 'Mobile' else -999

            # For DeviceInfo
            DeviceInfo = st.selectbox("Device Info", list(labels.keys()), key="DeviceInfo")
            DeviceInfo = labels[DeviceInfo]

            device_data = {"DeviceType": DeviceType, "DeviceInfo": DeviceInfo}

            st.divider() ############################################################################################################
            return device_data
        ```
    
    ```py
    device_data = deviceInfo(labels)
    ```

## Main Function of the Application 

```py
def app():
  st.write("This is a simple web app to predict whether a transaction is fraudulent or not.")  
  st.write("Please provide the necessary details to classify the transaction.")
  
  if st.button("Predict"):
    ...

    st.toast("Pre-processing has started...", icon="⏳")
    with st.spinner('Model is processing...'):
        ...

    st.toast("Pre-processing is complete...", icon="✅")

    with results:
      st.subheader("Results")
      st.toast("Model is working now...", icon="⏳")
      with st.spinner('Model is processing...'):
        ...

      st.toast("Prediction is complete...", icon="✅")
      try:
        prediction = predict(data)
        st.write(f'Hello {name}!')
        st.write('Based on the machine learning model, the risk of this transaction being fraudulent is:')
        if prediction[:,1] >= 0.5:
          st.error("**HIGH**", icon="🚫")
          st.toast("The transaction is classified as fraudulent.", icon="🚫")
        else:
          st.success("**LOW**", icon="✅")
          st.toast("The transaction is classified as non-fraudulent.", icon="🎉")
        
      except:
        st.error("Enter valid values to show the results.", icon="🚨")
        st.toast("Oops... Something went wrong. Please try again.", icon="🚨")
```

--- 

## Online Payment Fraud Detector 

<figure markdown="span">
    ![streamlit_app](https://github.com/user-attachments/assets/7e06b051-a1f1-427e-8c34-ec6d659ef498){ width="700" }
    <figcaption>[Powered By Streamlit](https://streamlit.io/)</figcaption>
</figure>

!!! success "Accuracy of the Model"

    The machine learning model used for prediction was initially evaluated on an unknown dataset 
    consisting of 506,691 records. The model correctly classified 89.54% of transactions as fraudulent and 
    88.66% of transactions as non-fraudulent. The model has an AUC-ROC score of 0.94. It also considers the cost of 
    misclassifying a non-fraudulent transaction as fraudulent, which is why the model is more likely to classify a transaction 
    as non-fraudulent rather than fraudulent.

!!! warning "Disclaimer"

    **The results from this test are not intended for any financial or legal advice.**
    The model was trained on 590,540 data points with personal attributes only. Additionally, the analysis of 
    this model indicates that attributes such as the transaction amount, maximum and minimum transaction limits, 
    and the distance of the transaction location are of high importance in determining if a transaction is fraudulent or not.

