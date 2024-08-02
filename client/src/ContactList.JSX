import React from "react"

const ConstactList = ({contacts}) => {
    return <div>
        <h2>Contacts</h2>
        <table>
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {contacts.map(contact => (
                    <tr key={contact.id}>
                        <td>{contact.first_name}</td>
                        <td>{contact.last_name}</td>
                        <td>{contact.email}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}