import React from 'react'
import meta from "../assets/248814656_249743847178667_2939325260132690749_n.gif"
import instagram from "../assets/instagram.png"

import "../styling/LoadingScreen.scss"

const LoadingScreen = () => {
  return (
    <div className='LoadingScreen_container'>
        <div className="LoadingScreen_meta-logo_container">
            <img src={instagram} alt="meta" />
        </div>
    </div>
  )
}

export default LoadingScreen