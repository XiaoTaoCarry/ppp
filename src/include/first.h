#ifndef CONFIG__H
#define CONFIG__H
#define KEY_LEN  (128/8)

#define ST_LEN  256

int sc_encrypt(char *pl_text, int pl_len, char *key, char *a, int *a_len);
int sc_decrypt(char *cp_text, int cp_len, char *key, char *m, int *m_len);

#endif