import { useState, useEffect } from 'react';
import ContactList from './ContactList';
import ContactForm from './ContactForm';
import './App.css';


function App() {
  const [contacts, setContacts] = useState([])

  useEffect(() => {
    fetchContacts() // as soon as this component loads, it calls this function. After it calls the functions it passes the valuex in the state, useState hook: setContacts
  }, [])

  const fetchContacts = async () => {
    const response = await fetch('http://127.0.0.1:5000/contacts')
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  }

  return (
    <>
  <ContactList contacts={contacts} /> 
  <ContactForm />  {/* This component will send data to our server */}
  </> 
  )
}

export default App
