func (sm *SessionManager) Decrypt(ct []byte, nonce []byte, iv []byte) ([]byte, error) {
            block, err := aes.NewCipher(sm.Key)

            if err != nil {
                return nil, fmt.Errorf("error while decrypting: %v", err)
            }

            ct2 := make([]byte, len(ct))
            mode := cipher.NewCBCDecrypter(block, iv)
            mode.CryptBlocks(ct2, ct)

            pt := make([]byte, len(ct2))
            mode2 := cipher.NewCTR(block, nonce)
            mode2.XORKeyStream(pt, ct2)

            // I've heard popular paddings lead to Padding Oracle
            idx := bytes.Index(pt, []byte("}"))
            if idx == -1 {
                return nil, fmt.Errorf("error while decrypting: no '}' in json")
            }

            return pt[:idx+1], nil
        }